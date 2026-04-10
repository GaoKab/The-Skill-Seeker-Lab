"""
NodeRail Storage Layer

JSON-file-based persistence for NodeRail's graph of intellectual work.
Stores nodes, edges, and version history in a single structured file.
"""

import json
import os
from typing import Optional

from .models import Node, Edge, Version


DEFAULT_STORE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "noderail_data.json",
)


def _empty_store() -> dict:
    return {"nodes": {}, "edges": {}, "versions": {}}


class NodeRailStore:
    """Persistent store for the NodeRail knowledge graph."""

    def __init__(self, path: str = DEFAULT_STORE_PATH):
        self.path = path
        self._data = self._load()

    # --- Persistence ---

    def _load(self) -> dict:
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return _empty_store()

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=2)

    # --- Nodes ---

    def add_node(self, node: Node) -> Node:
        self._data["nodes"][node.id] = node.to_dict()
        # Create initial version
        v = Version(
            node_id=node.id,
            version_number=1,
            evolution_type="refinement",
            title=node.title,
            description=node.description,
            changes="Initial creation",
            created_by=node.created_by,
        )
        self._data["versions"][v.id] = v.to_dict()
        self._save()
        return node

    def get_node(self, node_id: str) -> Optional[Node]:
        data = self._data["nodes"].get(node_id)
        if data:
            return Node.from_dict(data)
        return None

    def get_all_nodes(self) -> list[Node]:
        return [Node.from_dict(d) for d in self._data["nodes"].values()]

    def update_node(self, node: Node):
        self._data["nodes"][node.id] = node.to_dict()
        self._save()

    def delete_node(self, node_id: str):
        self._data["nodes"].pop(node_id, None)
        # Remove associated edges
        edge_ids_to_remove = [
            eid for eid, e in self._data["edges"].items()
            if e["source_id"] == node_id or e["target_id"] == node_id
        ]
        for eid in edge_ids_to_remove:
            del self._data["edges"][eid]
        # Remove associated versions
        ver_ids_to_remove = [
            vid for vid, v in self._data["versions"].items()
            if v["node_id"] == node_id
        ]
        for vid in ver_ids_to_remove:
            del self._data["versions"][vid]
        self._save()

    def get_nodes_by_type(self, node_type: str) -> list[Node]:
        return [
            Node.from_dict(d) for d in self._data["nodes"].values()
            if d["node_type"] == node_type
        ]

    def get_nodes_by_status(self, status: str) -> list[Node]:
        return [
            Node.from_dict(d) for d in self._data["nodes"].values()
            if d["status"] == status
        ]

    # --- Edges ---

    def add_edge(self, edge: Edge) -> Edge:
        self._data["edges"][edge.id] = edge.to_dict()
        self._save()
        return edge

    def get_all_edges(self) -> list[Edge]:
        return [Edge.from_dict(d) for d in self._data["edges"].values()]

    def get_edges_for_node(self, node_id: str) -> list[Edge]:
        return [
            Edge.from_dict(d) for d in self._data["edges"].values()
            if d["source_id"] == node_id or d["target_id"] == node_id
        ]

    def delete_edge(self, edge_id: str):
        self._data["edges"].pop(edge_id, None)
        self._save()

    # --- Versions ---

    def add_version(self, version: Version) -> Version:
        self._data["versions"][version.id] = version.to_dict()
        # Update the node's current version and timestamp
        node_data = self._data["nodes"].get(version.node_id)
        if node_data:
            node_data["current_version"] = version.version_number
            from .models import _now
            node_data["updated_at"] = _now()
        self._save()
        return version

    def get_versions_for_node(self, node_id: str) -> list[Version]:
        versions = [
            Version.from_dict(d) for d in self._data["versions"].values()
            if d["node_id"] == node_id
        ]
        return sorted(versions, key=lambda v: v.version_number)

    def get_latest_version(self, node_id: str) -> Optional[Version]:
        versions = self.get_versions_for_node(node_id)
        return versions[-1] if versions else None

    # --- Graph Queries ---

    def get_connected_nodes(self, node_id: str) -> list[tuple[Node, Edge]]:
        """Get all nodes connected to a given node, with their edges."""
        results = []
        for edge in self.get_edges_for_node(node_id):
            other_id = edge.target_id if edge.source_id == node_id else edge.source_id
            other_node = self.get_node(other_id)
            if other_node:
                results.append((other_node, edge))
        return results

    def get_lineage(self, node_id: str) -> list[tuple[Node, Edge]]:
        """Trace the lineage of a node — what it derives from, recursively."""
        visited = set()
        lineage = []

        def _trace(nid):
            if nid in visited:
                return
            visited.add(nid)
            for edge in self.get_edges_for_node(nid):
                if edge.source_id == nid and edge.relationship == "derives_from":
                    parent = self.get_node(edge.target_id)
                    if parent:
                        lineage.append((parent, edge))
                        _trace(parent.id)

        _trace(node_id)
        return lineage

    # --- Statistics ---

    def stats(self) -> dict:
        nodes = self.get_all_nodes()
        return {
            "total_nodes": len(nodes),
            "total_edges": len(self._data["edges"]),
            "total_versions": len(self._data["versions"]),
            "by_type": {
                nt: len([n for n in nodes if n.node_type == nt])
                for nt in ["concept", "framework", "measurement", "field_note", "inquiry", "project"]
            },
            "by_status": {
                s: len([n for n in nodes if n.status == s])
                for s in ["exploratory", "developing", "stable", "canonical", "archived"]
            },
        }
