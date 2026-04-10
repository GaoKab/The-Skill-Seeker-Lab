"""
NodeRail Storage Layer

JSON-file-based persistence for NodeRail's graph of intellectual work.
Stores nodes, edges, and version history in a single structured file.
"""

import json
import os
from typing import Optional

from .models import Node, Edge, Version, Institution, Member, Review


DEFAULT_STORE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "noderail_data.json",
)


def _empty_store() -> dict:
    return {
        "nodes": {}, "edges": {}, "versions": {},
        "institutions": {}, "members": {}, "reviews": {},
    }


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

    # --- Gap Detection / Structural Analysis ---

    def get_orphaned_nodes(self) -> list[Node]:
        """Nodes with zero connections — isolated from the graph."""
        all_edges = self.get_all_edges()
        connected_ids = set()
        for e in all_edges:
            connected_ids.add(e.source_id)
            connected_ids.add(e.target_id)
        return [n for n in self.get_all_nodes() if n.id not in connected_ids]

    def get_unsupported_frameworks(self) -> list[Node]:
        """Frameworks that have no concepts supporting them."""
        frameworks = self.get_nodes_by_type("framework")
        unsupported = []
        for fw in frameworks:
            edges = self.get_edges_for_node(fw.id)
            has_support = any(
                e.target_id == fw.id and e.relationship in ("supports", "derives_from")
                for e in edges
            )
            if not has_support:
                unsupported.append(fw)
        return unsupported

    def get_unmeasured_concepts(self) -> list[Node]:
        """Concepts that have no measurement connected to them."""
        concepts = self.get_nodes_by_type("concept")
        measurements = self.get_nodes_by_type("measurement")
        measurement_ids = {m.id for m in measurements}

        unmeasured = []
        for concept in concepts:
            edges = self.get_edges_for_node(concept.id)
            has_measurement = any(
                (e.source_id in measurement_ids or e.target_id in measurement_ids)
                for e in edges
            )
            if not has_measurement:
                unmeasured.append(concept)
        return unmeasured

    def get_unsupported_inquiries(self) -> list[Node]:
        """Inquiries with no supporting field notes or evidence."""
        inquiries = self.get_nodes_by_type("inquiry")
        field_notes = self.get_nodes_by_type("field_note")
        fn_ids = {fn.id for fn in field_notes}

        unsupported = []
        for inq in inquiries:
            edges = self.get_edges_for_node(inq.id)
            has_field_note = any(
                (e.source_id in fn_ids and e.target_id == inq.id)
                for e in edges
            )
            if not has_field_note:
                unsupported.append(inq)
        return unsupported

    def get_stale_nodes(self, max_version: int = 1) -> list[Node]:
        """Structures still at v1 with no evolution — never developed beyond creation."""
        return [
            n for n in self.get_all_nodes()
            if n.current_version <= max_version and n.status not in ("archived",)
        ]

    def get_long_exploratory(self) -> list[Node]:
        """Structures stuck in 'exploratory' status that have connections,
        suggesting they may be ready to advance to 'developing'."""
        exploratory = self.get_nodes_by_status("exploratory")
        ready = []
        for node in exploratory:
            edges = self.get_edges_for_node(node.id)
            if len(edges) >= 2:  # connected enough to potentially advance
                ready.append(node)
        return ready

    def get_unoperationalized_frameworks(self) -> list[Node]:
        """Frameworks with no project operationalizing them."""
        frameworks = self.get_nodes_by_type("framework")
        projects = self.get_nodes_by_type("project")
        project_ids = {p.id for p in projects}

        unop = []
        for fw in frameworks:
            edges = self.get_edges_for_node(fw.id)
            has_project = any(
                e.source_id in project_ids and e.relationship == "operationalizes"
                for e in edges
            )
            if not has_project:
                unop.append(fw)
        return unop

    def get_contradictions(self) -> list[tuple[Node, Node, Edge]]:
        """All 'challenges' relationships — active tensions in the system."""
        edges = self.get_all_edges()
        contradictions = []
        for e in edges:
            if e.relationship == "challenges":
                src = self.get_node(e.source_id)
                tgt = self.get_node(e.target_id)
                if src and tgt:
                    contradictions.append((src, tgt, e))
        return contradictions

    def get_hub_nodes(self, min_connections: int = 5) -> list[tuple[Node, int]]:
        """Most-connected structures — the hubs of the knowledge graph."""
        nodes = self.get_all_nodes()
        hubs = []
        for node in nodes:
            count = len(self.get_edges_for_node(node.id))
            if count >= min_connections:
                hubs.append((node, count))
        return sorted(hubs, key=lambda x: x[1], reverse=True)

    def run_full_analysis(self) -> dict:
        """Run all gap detection checks and return a structured report."""
        return {
            "orphaned": self.get_orphaned_nodes(),
            "unsupported_frameworks": self.get_unsupported_frameworks(),
            "unmeasured_concepts": self.get_unmeasured_concepts(),
            "unsupported_inquiries": self.get_unsupported_inquiries(),
            "stale": self.get_stale_nodes(),
            "long_exploratory": self.get_long_exploratory(),
            "unoperationalized": self.get_unoperationalized_frameworks(),
            "contradictions": self.get_contradictions(),
            "hubs": self.get_hub_nodes(),
        }

    # --- Institutions ---

    def add_institution(self, inst: Institution) -> Institution:
        if "institutions" not in self._data:
            self._data["institutions"] = {}
        self._data["institutions"][inst.id] = inst.to_dict()
        self._save()
        return inst

    def get_institution(self, inst_id: str) -> Optional[Institution]:
        if "institutions" not in self._data:
            return None
        data = self._data["institutions"].get(inst_id)
        return Institution.from_dict(data) if data else None

    def get_all_institutions(self) -> list[Institution]:
        if "institutions" not in self._data:
            return []
        return [Institution.from_dict(d) for d in self._data["institutions"].values()]

    # --- Members ---

    def add_member(self, member: Member) -> Member:
        if "members" not in self._data:
            self._data["members"] = {}
        self._data["members"][member.id] = member.to_dict()
        self._save()
        return member

    def get_member(self, member_id: str) -> Optional[Member]:
        if "members" not in self._data:
            return None
        data = self._data["members"].get(member_id)
        return Member.from_dict(data) if data else None

    def get_members_by_institution(self, inst_id: str) -> list[Member]:
        if "members" not in self._data:
            return []
        return [
            Member.from_dict(d) for d in self._data["members"].values()
            if d["institution_id"] == inst_id
        ]

    def get_all_members(self) -> list[Member]:
        if "members" not in self._data:
            return []
        return [Member.from_dict(d) for d in self._data["members"].values()]

    def get_reviewers(self) -> list[Member]:
        """Get all members with reviewer role."""
        if "members" not in self._data:
            return []
        return [
            Member.from_dict(d) for d in self._data["members"].values()
            if d["role"] == "reviewer"
        ]

    # --- Reviews ---

    def add_review(self, review: Review) -> Review:
        if "reviews" not in self._data:
            self._data["reviews"] = {}
        self._data["reviews"][review.id] = review.to_dict()
        self._save()
        return review

    def update_review(self, review: Review):
        if "reviews" not in self._data:
            self._data["reviews"] = {}
        self._data["reviews"][review.id] = review.to_dict()
        self._save()

    def get_review(self, review_id: str) -> Optional[Review]:
        if "reviews" not in self._data:
            return None
        data = self._data["reviews"].get(review_id)
        return Review.from_dict(data) if data else None

    def get_reviews_for_node(self, node_id: str) -> list[Review]:
        if "reviews" not in self._data:
            return []
        return [
            Review.from_dict(d) for d in self._data["reviews"].values()
            if d["node_id"] == node_id
        ]

    def get_reviews_by_reviewer(self, reviewer_id: str) -> list[Review]:
        if "reviews" not in self._data:
            return []
        return [
            Review.from_dict(d) for d in self._data["reviews"].values()
            if d["reviewer_id"] == reviewer_id
        ]

    def get_pending_reviews(self) -> list[Review]:
        if "reviews" not in self._data:
            return []
        return [
            Review.from_dict(d) for d in self._data["reviews"].values()
            if d["status"] in ("requested", "in_progress")
        ]

    def get_completed_reviews(self) -> list[Review]:
        if "reviews" not in self._data:
            return []
        return [
            Review.from_dict(d) for d in self._data["reviews"].values()
            if d["status"] == "completed"
        ]
