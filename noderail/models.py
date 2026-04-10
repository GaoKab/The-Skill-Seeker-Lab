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
        derives_from     — This work originates from a prior structure
        extends          — This work builds upon and expands existing work
        refines          — This work sharpens or clarifies existing work
        challenges       — This work questions or contradicts existing work
        applies_to       — This work is used in a specific domain or context
        supports         — This work strengthens or underpins existing work
        operationalizes  — This work makes a framework or concept actionable
        diverges_from    — This work breaks away to form a new direction

    Evolution Types (Versions):
        refinement        — Sharpening precision without changing direction
        extension         — Adding new dimensions or scope
        reinterpretation  — Recasting meaning in a new light
        application       — Moving from theory to practice
        divergence        — Breaking from the original trajectory
        split             — One object becomes multiple more specific objects
        merge             — Several objects brought together into a coherent whole

    Status Levels:
        exploratory — Early thinking, still open and unstable
        developing  — Actively being shaped and extended
        stable      — Mature, a working reference point
        canonical   — Central, trusted, authoritative version
        archived    — No longer current, preserved for lineage
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
    ("refines", "Refines", "This work sharpens or clarifies existing work"),
    ("challenges", "Challenges", "This work questions or contradicts existing work"),
    ("applies_to", "Applies to", "This work is used in a specific domain or context"),
    ("supports", "Supports", "This work strengthens or underpins existing work"),
    ("operationalizes", "Operationalizes", "This work makes a framework or concept actionable"),
    ("diverges_from", "Diverges from", "This work breaks away to form a new direction"),
]

EVOLUTION_TYPES = [
    ("refinement", "Refinement", "Sharpening precision without changing direction"),
    ("extension", "Extension", "Adding new dimensions or scope"),
    ("reinterpretation", "Reinterpretation", "Recasting meaning in a new light"),
    ("application", "Application", "Moving from theory to practice"),
    ("divergence", "Divergence", "Breaking from the original trajectory"),
    ("split", "Split", "One object becomes multiple more specific objects"),
    ("merge", "Merge", "Several objects brought together into a coherent whole"),
]

STATUS_LEVELS = [
    ("exploratory", "Exploratory", "Early thinking, still open and unstable"),
    ("developing", "Developing", "Actively being shaped and extended"),
    ("stable", "Stable", "Mature, a working reference point"),
    ("canonical", "Canonical", "Central, trusted, authoritative version"),
    ("archived", "Archived", "No longer current, preserved for lineage"),
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
    status: str = "exploratory"
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
            status=data.get("status", "exploratory"),
            tags=data.get("tags", []),
            current_version=data.get("current_version", 1),
        )


@dataclass
class Edge:
    """A typed relationship between two nodes."""
    source_id: str
    target_id: str
    relationship: str  # derives_from, extends, refines, challenges, applies_to, supports, operationalizes, diverges_from
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
    evolution_type: str  # refinement, extension, reinterpretation, application, divergence, split, merge
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


# --- Institution & Review Models ---

INSTITUTION_TYPES = [
    ("university", "University", "Academic institution"),
    ("research_lab", "Research Lab", "Dedicated research organization"),
    ("think_tank", "Think Tank", "Policy or strategy research organization"),
    ("corporate_rd", "Corporate R&D", "Corporate research and development"),
    ("government", "Government Agency", "Government-funded research body"),
    ("independent", "Independent", "Independent research collective or studio"),
]

MEMBER_ROLES = [
    ("admin", "Admin", "Manages the institution on NodeRail"),
    ("researcher", "Researcher", "Publishes and develops work"),
    ("reviewer", "Reviewer", "Reviews and evaluates work"),
    ("reader", "Reader", "Browses and cites work"),
]

REVIEW_STATUSES = [
    ("requested", "Requested", "Review has been requested"),
    ("in_progress", "In Progress", "Reviewer is evaluating"),
    ("completed", "Completed", "Review is complete"),
    ("declined", "Declined", "Reviewer declined the request"),
]

REVIEW_VERDICTS = [
    ("validated", "Validated", "Work meets the required level of rigor"),
    ("needs_revision", "Needs Revision", "Work has merit but requires changes"),
    ("novel", "Novel", "Work represents a genuinely new contribution"),
    ("not_ready", "Not Ready", "Work is not yet at the required level"),
]


@dataclass
class Institution:
    """An organization with members who publish and review on NodeRail."""
    name: str
    institution_type: str
    description: str
    id: str = field(default_factory=_uuid)
    created_at: str = field(default_factory=_now)
    website: str = ""
    contact_email: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "institution_type": self.institution_type,
            "description": self.description,
            "created_at": self.created_at,
            "website": self.website,
            "contact_email": self.contact_email,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Institution":
        return cls(
            id=data["id"],
            name=data["name"],
            institution_type=data["institution_type"],
            description=data["description"],
            created_at=data["created_at"],
            website=data.get("website", ""),
            contact_email=data.get("contact_email", ""),
        )


@dataclass
class Member:
    """A person affiliated with an institution on NodeRail."""
    name: str
    institution_id: str
    role: str  # admin, researcher, reviewer, reader
    id: str = field(default_factory=_uuid)
    created_at: str = field(default_factory=_now)
    expertise: str = ""
    email: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "institution_id": self.institution_id,
            "role": self.role,
            "created_at": self.created_at,
            "expertise": self.expertise,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Member":
        return cls(
            id=data["id"],
            name=data["name"],
            institution_id=data["institution_id"],
            role=data["role"],
            created_at=data["created_at"],
            expertise=data.get("expertise", ""),
            email=data.get("email", ""),
        )


@dataclass
class Review:
    """An expert evaluation of a structure on NodeRail.
    Permanently attached to the node's lineage."""
    node_id: str
    reviewer_id: str  # Member ID
    verdict: str  # validated, needs_revision, novel, not_ready
    status: str = "requested"
    id: str = field(default_factory=_uuid)
    created_at: str = field(default_factory=_now)
    completed_at: str = ""
    # Structured evaluation
    is_rigorous: str = ""       # Is this at the required level of rigor?
    is_novel: str = ""          # Is this genuinely new?
    what_is_missing: str = ""   # What needs to change?
    summary: str = ""           # Overall assessment
    requested_by: str = ""      # Member ID of who requested

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "node_id": self.node_id,
            "reviewer_id": self.reviewer_id,
            "verdict": self.verdict,
            "status": self.status,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
            "is_rigorous": self.is_rigorous,
            "is_novel": self.is_novel,
            "what_is_missing": self.what_is_missing,
            "summary": self.summary,
            "requested_by": self.requested_by,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Review":
        return cls(
            id=data["id"],
            node_id=data["node_id"],
            reviewer_id=data["reviewer_id"],
            verdict=data.get("verdict", ""),
            status=data.get("status", "requested"),
            created_at=data["created_at"],
            completed_at=data.get("completed_at", ""),
            is_rigorous=data.get("is_rigorous", ""),
            is_novel=data.get("is_novel", ""),
            what_is_missing=data.get("what_is_missing", ""),
            summary=data.get("summary", ""),
            requested_by=data.get("requested_by", ""),
        )
