"""
NodeRail Graph Visualization

Generates interactive HTML graph visualizations of the NodeRail
knowledge network using pyvis. Designed to render inside Streamlit
via st.components.v1.html.
"""

import json
import tempfile
from typing import Optional

from .models import Node, Edge


# Color palette — muted, disciplined tones
NODE_COLORS = {
    "concept": "#4A6FA5",      # steel blue
    "framework": "#6B4C9A",    # muted purple
    "measurement": "#2E7D6F",  # teal
    "field_note": "#8B6914",   # dark gold
    "inquiry": "#A0522D",      # sienna
    "project": "#555555",      # slate gray
}

NODE_SHAPES = {
    "concept": "dot",
    "framework": "diamond",
    "measurement": "triangle",
    "field_note": "square",
    "inquiry": "star",
    "project": "hexagon",
}

EDGE_COLORS = {
    "derives_from": "#888888",
    "extends": "#4A6FA5",
    "challenges": "#C0392B",
    "applies_to": "#2E7D6F",
    "diverges_from": "#8B6914",
}

STATUS_BORDER = {
    "draft": "#AAAAAA",
    "active": "#4A6FA5",
    "stable": "#2E7D6F",
    "canonical": "#6B4C9A",
    "archived": "#666666",
}


def build_graph_html(
    nodes: list[Node],
    edges: list[Edge],
    highlight_node_id: Optional[str] = None,
    height: str = "500px",
    width: str = "100%",
) -> str:
    """Build an interactive network graph as raw HTML/JS using vis.js CDN."""

    vis_nodes = []
    for node in nodes:
        color = NODE_COLORS.get(node.node_type, "#888888")
        border = STATUS_BORDER.get(node.status, "#AAAAAA")
        size = 30 if node.id == highlight_node_id else 20

        vis_nodes.append({
            "id": node.id,
            "label": node.title,
            "color": {
                "background": color,
                "border": border,
                "highlight": {"background": color, "border": "#FFFFFF"},
            },
            "shape": NODE_SHAPES.get(node.node_type, "dot"),
            "size": size,
            "font": {"color": "#E0E0E0", "size": 12},
            "title": f"<b>{node.title}</b><br>Type: {node.node_type}<br>Status: {node.status}<br>{node.description[:120]}",
        })

    vis_edges = []
    for edge in edges:
        color = EDGE_COLORS.get(edge.relationship, "#888888")
        label_map = {
            "derives_from": "derives from",
            "extends": "extends",
            "challenges": "challenges",
            "applies_to": "applies to",
            "diverges_from": "diverges from",
        }
        vis_edges.append({
            "from": edge.source_id,
            "to": edge.target_id,
            "label": label_map.get(edge.relationship, edge.relationship),
            "color": {"color": color, "highlight": "#FFFFFF"},
            "arrows": "to",
            "font": {"color": "#999999", "size": 10, "strokeWidth": 0},
            "smooth": {"type": "curvedCW", "roundness": 0.2},
        })

    nodes_json = json.dumps(vis_nodes)
    edges_json = json.dumps(vis_edges)

    html = f"""
    <html>
    <head>
        <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background: #0E1117;
                overflow: hidden;
            }}
            #graph {{
                width: {width};
                height: {height};
                background: #0E1117;
                border: 1px solid #2A2A2A;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <div id="graph"></div>
        <script>
            var nodes = new vis.DataSet({nodes_json});
            var edges = new vis.DataSet({edges_json});
            var container = document.getElementById("graph");
            var data = {{ nodes: nodes, edges: edges }};
            var options = {{
                physics: {{
                    barnesHut: {{
                        gravitationalConstant: -3000,
                        centralGravity: 0.3,
                        springLength: 150,
                        springConstant: 0.04,
                        damping: 0.09,
                    }},
                    stabilization: {{ iterations: 150 }},
                }},
                interaction: {{
                    hover: true,
                    tooltipDelay: 200,
                    zoomView: true,
                    dragView: true,
                }},
                edges: {{
                    width: 1.5,
                    selectionWidth: 3,
                }},
                nodes: {{
                    borderWidth: 2,
                    borderWidthSelected: 3,
                }},
            }};
            var network = new vis.Network(container, data, options);
        </script>
    </body>
    </html>
    """
    return html


def build_lineage_html(
    node: Node,
    versions: list,
    height: str = "300px",
) -> str:
    """Build a horizontal timeline visualization of a node's version history."""

    if not versions:
        return "<p style='color:#888;'>No version history yet.</p>"

    evo_colors = {
        "refinement": "#4A6FA5",
        "extension": "#6B4C9A",
        "reinterpretation": "#8B6914",
        "application": "#2E7D6F",
        "divergence": "#C0392B",
    }

    items_html = ""
    for i, v in enumerate(versions):
        color = evo_colors.get(v.evolution_type, "#888888")
        is_first = i == 0
        is_last = i == len(versions) - 1
        items_html += f"""
        <div style="display:inline-block; text-align:center; margin:0 8px; vertical-align:top;">
            <div style="
                width:14px; height:14px; border-radius:50%;
                background:{color}; border:2px solid {'#FFF' if is_last else '#555'};
                margin:0 auto 6px auto;
            "></div>
            <div style="font-size:11px; color:#CCC; font-weight:{'bold' if is_last else 'normal'};">
                v{v.version_number}
            </div>
            <div style="font-size:10px; color:#888; max-width:100px; word-wrap:break-word;">
                {v.evolution_type}
            </div>
            <div style="font-size:9px; color:#666; max-width:100px; word-wrap:break-word; margin-top:2px;">
                {v.changes[:50]}
            </div>
        </div>
        {"<div style='display:inline-block; vertical-align:top; margin-top:5px; color:#444;'>→</div>" if not is_last else ""}
        """

    return f"""
    <div style="
        background:#0E1117; border:1px solid #2A2A2A; border-radius:8px;
        padding:20px; overflow-x:auto; white-space:nowrap;
    ">
        <div style="font-size:12px; color:#666; margin-bottom:12px; letter-spacing:1px; text-transform:uppercase;">
            Lineage — {node.title}
        </div>
        {items_html}
    </div>
    """
