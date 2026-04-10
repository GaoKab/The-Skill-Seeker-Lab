"""
NodeRail Export Layer

Generates shareable artifacts from the NodeRail knowledge graph:
- Markdown: individual structure with full context
- HTML: standalone interactive graph
- JSON: portable graph data
"""

import json
from datetime import datetime, timezone

from .models import (
    Node, Edge, Version,
    NODE_TYPES, RELATIONSHIP_TYPES, EVOLUTION_TYPES, STATUS_LEVELS,
)
from .storage import NodeRailStore
from .graph_utils import build_graph_html


# --- Helpers ---

_type_label = dict((t[0], t[1]) for t in NODE_TYPES)
_rel_label = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES)
_evo_label = dict((e[0], e[1]) for e in EVOLUTION_TYPES)
_status_label = dict((s[0], s[1]) for s in STATUS_LEVELS)


def _timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


# ===================================================================
# MARKDOWN EXPORT — Single Structure
# ===================================================================

def export_node_markdown(store: NodeRailStore, node_id: str) -> str:
    """Export a single structure with its full context as clean markdown."""
    node = store.get_node(node_id)
    if not node:
        return "# Error\n\nStructure not found."

    lines = []

    # Header
    lines.append(f"# {node.title}")
    lines.append("")
    lines.append(
        f"**Type:** {_type_label.get(node.node_type, node.node_type)}  "
    )
    lines.append(
        f"**Status:** {_status_label.get(node.status, node.status)}  "
    )
    lines.append(f"**Version:** v{node.current_version}  ")
    lines.append(f"**Created:** {node.created_at[:10]}  ")
    lines.append(f"**Last updated:** {node.updated_at[:10]}  ")
    if node.tags:
        lines.append(f"**Tags:** {', '.join(node.tags)}  ")
    lines.append("")

    # Description
    lines.append("## Definition")
    lines.append("")
    lines.append(node.description)
    lines.append("")

    # Upstream lineage (where it came from)
    incoming = [
        (other, edge) for other, edge in store.get_connected_nodes(node.id)
        if edge.target_id == node.id
    ]
    if incoming:
        lines.append("## Where it came from")
        lines.append("")
        for other, edge in incoming:
            rel = _rel_label.get(edge.relationship, edge.relationship)
            t = _type_label.get(other.node_type, other.node_type)
            lines.append(f"- **{other.title}** ({t}) — *{rel}*")
            if edge.description:
                lines.append(f"  - {edge.description}")
        lines.append("")

    # Downstream influence (what it shaped)
    outgoing = [
        (other, edge) for other, edge in store.get_connected_nodes(node.id)
        if edge.source_id == node.id
    ]
    if outgoing:
        lines.append("## What it influenced")
        lines.append("")
        for other, edge in outgoing:
            rel = _rel_label.get(edge.relationship, edge.relationship)
            t = _type_label.get(other.node_type, other.node_type)
            lines.append(f"- *{rel}* → **{other.title}** ({t})")
            if edge.description:
                lines.append(f"  - {edge.description}")
        lines.append("")

    # Evolution history
    versions = store.get_versions_for_node(node.id)
    if versions and len(versions) > 1:
        lines.append("## Evolution history")
        lines.append("")
        for v in versions:
            evo = _evo_label.get(v.evolution_type, v.evolution_type)
            lines.append(f"### v{v.version_number} — {evo}")
            lines.append("")
            lines.append(v.changes)
            lines.append("")
            lines.append(f"*{v.created_at[:10]}*")
            lines.append("")

    # Lineage trace
    lineage = store.get_lineage(node.id)
    if lineage:
        lines.append("## Lineage")
        lines.append("")
        chain = [node.title]
        for ancestor, edge in lineage:
            chain.append(ancestor.title)
        lines.append(" → ".join(chain))
        lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append(f"*Exported from NodeRail — {_timestamp()}*")

    return "\n".join(lines)


# ===================================================================
# MARKDOWN EXPORT — Full Graph Summary
# ===================================================================

def export_graph_markdown(store: NodeRailStore) -> str:
    """Export the entire knowledge graph as a structured markdown document."""
    nodes = store.get_all_nodes()
    edges = store.get_all_edges()
    stats = store.stats()

    lines = []

    lines.append("# NodeRail — Knowledge Graph Export")
    lines.append("")
    lines.append(f"*Exported: {_timestamp()}*")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **{stats['total_nodes']}** structures")
    lines.append(f"- **{stats['total_edges']}** connections")
    lines.append(f"- **{stats['total_versions']}** versions")
    lines.append("")

    # By type
    lines.append("### By type")
    lines.append("")
    for nt in ["framework", "concept", "measurement", "inquiry", "project", "field_note"]:
        count = stats["by_type"].get(nt, 0)
        if count > 0:
            label = _type_label.get(nt, nt)
            lines.append(f"- {label}: {count}")
    lines.append("")

    # By status
    lines.append("### By status")
    lines.append("")
    for st_key in ["exploratory", "developing", "stable", "canonical", "archived"]:
        count = stats["by_status"].get(st_key, 0)
        if count > 0:
            label = _status_label.get(st_key, st_key)
            lines.append(f"- {label}: {count}")
    lines.append("")

    # Group by type
    type_order = ["framework", "concept", "measurement", "inquiry", "project", "field_note"]
    for nt in type_order:
        type_nodes = sorted(
            [n for n in nodes if n.node_type == nt],
            key=lambda n: n.title,
        )
        if not type_nodes:
            continue

        label = _type_label.get(nt, nt) + "s"
        lines.append(f"## {label}")
        lines.append("")

        for node in type_nodes:
            status = _status_label.get(node.status, node.status)
            lines.append(f"### {node.title}")
            lines.append("")
            lines.append(
                f"*{status} · v{node.current_version} · "
                f"Created {node.created_at[:10]}*"
            )
            lines.append("")
            lines.append(node.description)
            lines.append("")

            # Connections
            connected = store.get_connected_nodes(node.id)
            if connected:
                lines.append("**Connections:**")
                for other, edge in connected:
                    rel = _rel_label.get(edge.relationship, edge.relationship)
                    direction = "→" if edge.source_id == node.id else "←"
                    lines.append(f"- {direction} *{rel}* **{other.title}**")
                lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append(f"*Exported from NodeRail — {_timestamp()}*")

    return "\n".join(lines)


# ===================================================================
# HTML EXPORT — Standalone Interactive Graph
# ===================================================================

def export_graph_html(store: NodeRailStore) -> str:
    """Export the full graph as a standalone HTML file with embedded vis.js."""
    nodes = store.get_all_nodes()
    edges = store.get_all_edges()
    stats = store.stats()

    graph_html = build_graph_html(nodes, edges, height="100vh", width="100%")

    # Wrap with a proper standalone page
    title = "NodeRail — Knowledge Graph"
    timestamp = _timestamp()

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: #0E1117;
            color: #E0E0E0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }}
        #header {{
            padding: 16px 24px;
            border-bottom: 1px solid #1E2230;
        }}
        #header h1 {{
            margin: 0;
            font-size: 1.4em;
            font-weight: 300;
            letter-spacing: 1px;
        }}
        #header p {{
            margin: 4px 0 0 0;
            color: #666;
            font-size: 0.85em;
        }}
        #stats {{
            padding: 8px 24px;
            background: #141820;
            border-bottom: 1px solid #1E2230;
            font-size: 0.8em;
            color: #888;
        }}
        #graph-container {{
            width: 100%;
            height: calc(100vh - 100px);
        }}
    </style>
</head>
<body>
    <div id="header">
        <h1>&#9670; NodeRail</h1>
        <p>Knowledge Graph — {stats['total_nodes']} structures · {stats['total_edges']} connections</p>
    </div>
    <div id="stats">
        Exported {timestamp}
    </div>
    <div id="graph-container">
        {graph_html}
    </div>
</body>
</html>"""

    return html


# ===================================================================
# JSON EXPORT — Portable Graph Data
# ===================================================================

def export_graph_json(store: NodeRailStore) -> str:
    """Export the full graph as structured JSON for portability."""
    nodes = store.get_all_nodes()
    edges = store.get_all_edges()

    # Collect all versions
    all_versions = []
    for node in nodes:
        all_versions.extend(store.get_versions_for_node(node.id))

    data = {
        "noderail_export": {
            "version": "1.0",
            "exported_at": _timestamp(),
            "stats": store.stats(),
        },
        "nodes": [n.to_dict() for n in nodes],
        "edges": [e.to_dict() for e in edges],
        "versions": [v.to_dict() for v in all_versions],
    }

    return json.dumps(data, indent=2)
