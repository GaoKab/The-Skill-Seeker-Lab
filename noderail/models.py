"""
NodeRail Core Data Models

The object model for NodeRail uses precise vocabulary that reflects
the intellectual seriousness of the work it structures:

    Node Types:
        concept     — A discrete unit of thought or theory
        framework   — A structured system of interrelated concepts
        measurement — A defined metric, scale, or assessment instrument
        field_note  — An observation, finding, or grounded insight
        inquiry     — A question, research thread, or line of investigation
        project     — A bounded initiative applying one or more frameworks

    Relationship Types (Edges):
        derives_from  — This work originates from a prior structure
        extends       — This work builds upon and expands existing work
        challenges    — This work questions or contradicts existing work
        applies_to    — This work operationalizes or implements existing work
        diverges_from — This work breaks away to form a new direction

    Evolution Types (Versions):
        refinement        — Sharpening precision without changing direction
        extension         — Adding new dimensions or scope
        reinterpretation  — Recasting meaning in a new light
        application       — Moving from theory to practice
        divergence        — Breaking from the original trajectory

    Status Levels:
        draft      — Work in progress, not yet stable
        active     — Under development, open to evolution
        stable     — Mature, unlikely to change significantly
        canonical  — Curated, authoritative version
        archived   — Preserved but no longer active
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
import uuid


# --- Constants ---

NODE_TYPES = [
    ("concept", "Concept", "A discrete unit of thought or theory"),
    ("framework", "Framework", "A structured system of interrelated concepts"),
    ("measurement", "Measurement", "A defined metric, scale, or assessment instrument"),
    ("field_note", "Field Note", "An observation, finding, or grounded insight"),
    ("inquiry", "Inquiry", "A question, research thread, or line of investigation"),
    ("project", "Project", "A bounded initiative applying one or more frameworks"),
]

RELATIONSHIP_TYPES = [
    ("derives_from", "Derives from", "This work originates from a prior structure"),
    ("extends", "Extends", "This work builds upon and expands existing work"),
    ("challenges", "Challenges", "This work questions or contradicts existing work"),
    ("applies_to", "Applies to", "This work operationalizes or implements existing work"),
    ("diverges_from", "Diverges from", "This work breaks away to form a new direction"),
]

EVOLUTION_TYPES = [
    ("refinement", "Refinement", "Sharpening precision without changing direction"),
    ("extension", "Extension", "Adding new dimensions or scope"),
    ("reinterpretation", "Reinterpretation", "Recasting meaning in a new light"),
    ("application", "Application", "Moving from theory to practice"),
    ("divergence", "Divergence", "Breaking from the original trajectory"),
]

STATUS_LEVELS = [
    ("draft", "Draft", "Work in progress, not yet stable"),
    ("active", "Active", "Under development, open to evolution"),
    ("stable", "Stable", "Mature, unlikely to change significantly"),
    ("canonical", "Canonical", "Curated, authoritative version"),
    ("archived", "Archived", "Preserved but no longer active"),
]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _uuid() -> str:
    return str(uuid.uuid4())


# --- Data Classes ---

@dataclass
class Node:
    """A unit of intellectual work within NodeRail."""
    title: str
    description: str
    node_type: str  # concept, framework, measurement, field_note, inquiry, project
    id: str = field(default_factory=_uuid)
    created_at: str = field(default_factory=_now)
    updated_at: str = field(default_factory=_now)
    created_by: str = "author"
    status: str = "draft"
    tags: list[str] = field(default_factory=list)
    current_version: int = 1

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "node_type": self.node_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "status": self.status,
            "tags": self.tags,
            "current_version": self.current_version,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Node":
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            node_type=data["node_type"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            created_by=data.get("created_by", "author"),
            status=data.get("status", "draft"),
            tags=data.get("tags", []),
            current_version=data.get("current_version", 1),
        )


@dataclass
class Edge:
    """A typed relationship between two nodes."""
    source_id: str
    target_id: str
    relationship: str  # derives_from, extends, challenges, applies_to, diverges_from
    id: str = field(default_factory=_uuid)
    created_at: str = field(default_factory=_now)
    description: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "relationship": self.relationship,
            "created_at": self.created_at,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Edge":
        return cls(
            id=data["id"],
            source_id=data["source_id"],
            target_id=data["target_id"],
            relationship=data["relationship"],
            created_at=data["created_at"],
            description=data.get("description", ""),
        )


@dataclass
class Version:
    """A tracked evolution of a node. Every change creates lineage."""
    node_id: str
    version_number: int
    evolution_type: str  # refinement, extension, reinterpretation, application, divergence
    title: str
    description: str
    changes: str  # What specifically changed
    id: str = field(default_factory=_uuid)
    created_at: str = field(default_factory=_now)
    created_by: str = "author"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "node_id": self.node_id,
            "version_number": self.version_number,
            "evolution_type": self.evolution_type,
            "title": self.title,
            "description": self.description,
            "changes": self.changes,
            "created_at": self.created_at,
            "created_by": self.created_by,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Version":
        return cls(
            id=data["id"],
            node_id=data["node_id"],
            version_number=data["version_number"],
            evolution_type=data["evolution_type"],
            title=data["title"],
            description=data["description"],
            changes=data["changes"],
            created_at=data["created_at"],
            created_by=data.get("created_by", "author"),
        )
