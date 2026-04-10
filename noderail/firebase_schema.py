"""
NodeRail Firebase Data Model Specification

Maps the Streamlit prototype data model to Firestore collections
for deployment on noderail.web.app.

This document defines:
1. Firestore collection structure
2. Field-by-field mapping from prototype to production
3. Security rules outline
4. Role-based access model
5. DOI integration points

Generated from the working Streamlit prototype at:
  /noderail/models.py
  /noderail/storage.py
"""


# ===================================================================
# FIRESTORE COLLECTIONS
# ===================================================================

FIRESTORE_SCHEMA = {

    # -----------------------------------------------------------------
    # NODES — Core intellectual objects
    # -----------------------------------------------------------------
    # Collection: /nodes/{nodeId}
    "nodes": {
        "id": "string (auto-generated Firestore ID)",
        "title": "string",
        "description": "string",
        "node_type": "string (concept | framework | measurement | field_note | inquiry | project)",
        "status": "string (exploratory | developing | stable | canonical | archived)",
        "created_at": "timestamp",
        "updated_at": "timestamp",
        "created_by": "string (userId reference)",
        "current_version": "number",
        "tags": "array<string>",
        "field_id": "string (reference to the field this node belongs to, e.g., HCS)",
        "institution_id": "string (optional, institution affiliation)",
        "doi": "string (optional, assigned after review)",
        "is_public": "boolean (default true)",
    },

    # -----------------------------------------------------------------
    # EDGES — Typed relationships between nodes
    # -----------------------------------------------------------------
    # Collection: /edges/{edgeId}
    "edges": {
        "id": "string",
        "source_id": "string (nodeId reference)",
        "target_id": "string (nodeId reference)",
        "relationship": "string (derives_from | extends | refines | challenges | applies_to | supports | operationalizes | diverges_from)",
        "description": "string (optional context)",
        "created_at": "timestamp",
        "created_by": "string (userId reference)",
    },

    # -----------------------------------------------------------------
    # VERSIONS — Evolution history (subcollection of nodes)
    # -----------------------------------------------------------------
    # Collection: /nodes/{nodeId}/versions/{versionId}
    "versions": {
        "id": "string",
        "version_number": "number",
        "evolution_type": "string (refinement | extension | reinterpretation | application | divergence | split | merge)",
        "title": "string (title at this version)",
        "description": "string (description at this version)",
        "changes": "string (what specifically changed)",
        "created_at": "timestamp",
        "created_by": "string (userId reference)",
        "doi": "string (optional, DOI for this specific version)",
    },

    # -----------------------------------------------------------------
    # USERS — Authenticated users
    # -----------------------------------------------------------------
    # Collection: /users/{userId}
    "users": {
        "id": "string (Firebase Auth UID)",
        "display_name": "string",
        "email": "string",
        "role": "string (reader | contributor | field_founder)",
        "institution_id": "string (optional)",
        "expertise": "string",
        "orcid": "string (optional, ORCID ID for academic identity)",
        "created_at": "timestamp",
        "node_count": "number (how many nodes published)",
        "review_count": "number (how many reviews completed)",
    },

    # -----------------------------------------------------------------
    # INSTITUTIONS — Organizations on NodeRail
    # -----------------------------------------------------------------
    # Collection: /institutions/{institutionId}
    "institutions": {
        "id": "string",
        "name": "string",
        "institution_type": "string (university | research_lab | think_tank | corporate_rd | government | independent)",
        "description": "string",
        "website": "string",
        "contact_email": "string",
        "created_at": "timestamp",
        "admin_ids": "array<string> (userId references)",
        "member_count": "number",
        "plan": "string (free | standard | enterprise)",
    },

    # -----------------------------------------------------------------
    # MEMBERS — Institution membership (subcollection)
    # -----------------------------------------------------------------
    # Collection: /institutions/{institutionId}/members/{memberId}
    "members": {
        "user_id": "string (userId reference)",
        "role": "string (admin | researcher | reviewer | reader)",
        "joined_at": "timestamp",
        "expertise": "string",
    },

    # -----------------------------------------------------------------
    # REVIEWS — Expert evaluations
    # -----------------------------------------------------------------
    # Collection: /reviews/{reviewId}
    "reviews": {
        "id": "string",
        "node_id": "string (nodeId reference)",
        "reviewer_id": "string (userId reference)",
        "requested_by": "string (userId reference)",
        "status": "string (requested | in_progress | completed | declined)",
        "verdict": "string (validated | needs_revision | novel | not_ready)",
        "created_at": "timestamp",
        "completed_at": "timestamp (optional)",
        # Structured evaluation
        "is_rigorous": "string",
        "is_novel": "string",
        "what_is_missing": "string",
        "summary": "string",
        # Review permanence
        "is_public": "boolean (default true, reviews are lineage)",
    },

    # -----------------------------------------------------------------
    # FIELDS — Top-level knowledge domains
    # -----------------------------------------------------------------
    # Collection: /fields/{fieldId}
    # Maps to what the website calls "Founder Fields"
    "fields": {
        "id": "string",
        "name": "string (e.g., Human Capacity Science)",
        "description": "string",
        "founder_id": "string (userId reference)",
        "created_at": "timestamp",
        "status": "string (draft | active | published)",
        "doi": "string (field-level DOI)",
        "node_count": "number",
        "continuity_standard_version": "string (e.g., v0.1)",
    },

    # -----------------------------------------------------------------
    # DOIS — DOI registry
    # -----------------------------------------------------------------
    # Collection: /dois/{doiId}
    "dois": {
        "doi": "string (the DOI itself, e.g., 10.5281/zenodo.XXXXXXX)",
        "target_type": "string (node | version | field)",
        "target_id": "string",
        "issued_at": "timestamp",
        "issued_by": "string (system or userId)",
        "zenodo_deposit_id": "string",
        "metadata": {
            "title": "string",
            "creators": "array<string>",
            "description": "string",
            "keywords": "array<string>",
            "version": "string",
        },
    },
}


# ===================================================================
# ROLE-BASED ACCESS
# ===================================================================

ROLE_PERMISSIONS = {
    "reader": {
        "can_read": True,
        "can_create": False,
        "can_edit_own": False,
        "can_review": False,
        "can_admin": False,
        "description": "Browse, cite, and trace lineage. No publishing.",
    },
    "contributor": {
        "can_read": True,
        "can_create": True,
        "can_edit_own": True,
        "can_review": False,
        "can_admin": False,
        "description": "Publish nodes, extend existing work, request reviews.",
    },
    "reviewer": {
        "can_read": True,
        "can_create": True,
        "can_edit_own": True,
        "can_review": True,
        "can_admin": False,
        "description": "All contributor permissions plus evaluate and review.",
    },
    "field_founder": {
        "can_read": True,
        "can_create": True,
        "can_edit_own": True,
        "can_review": True,
        "can_admin": False,
        "can_create_field": True,
        "can_manage_canon": True,
        "description": "Creates new fields. Governs what becomes canonical.",
    },
    "institution_admin": {
        "can_read": True,
        "can_create": True,
        "can_edit_own": True,
        "can_review": False,
        "can_admin": True,
        "can_manage_members": True,
        "description": "Manages institutional membership and settings.",
    },
}


# ===================================================================
# ROLE TRANSITIONS (from the website)
# ===================================================================

ROLE_TRANSITIONS = {
    "reader_to_contributor": "A Reader becomes a Contributor the moment they publish a node.",
    "contributor_to_field_founder": "A Contributor becomes a Field Founder the moment they create a new field.",
    "anyone_to_reviewer": "Reviewer status is granted by institution admins or platform admins.",
}


# ===================================================================
# DOI INTEGRATION POINTS
# ===================================================================

DOI_WORKFLOW = {
    "trigger": "DOI is issued when a node reaches 'stable' or 'canonical' status AND has at least one completed expert review.",
    "provider": "Zenodo (via API)",
    "metadata_source": "Node title, description, creator, tags, version, field, institution",
    "versioning": "Each major version can receive its own DOI. The node-level DOI resolves to the latest stable version.",
    "linkage": "DOI metadata includes 'isPartOf' relationship to the field DOI and 'isDerivedFrom' for lineage.",
}


# ===================================================================
# DOI-REVIEW INTEGRATION — Full Pipeline
# ===================================================================

DOI_REVIEW_PIPELINE = {
    "overview": (
        "DOI issuance is gated by expert review. This ensures that "
        "every DOI-backed artifact on NodeRail has been evaluated "
        "for rigor and novelty. The pipeline creates a quality "
        "signal that makes NodeRail DOIs more credible than "
        "self-published DOIs on generic platforms."
    ),

    "stages": [
        {
            "stage": 1,
            "name": "Creation",
            "status": "exploratory",
            "doi": False,
            "description": (
                "Author creates a node. No DOI issued. "
                "Work is visible but clearly marked as exploratory."
            ),
        },
        {
            "stage": 2,
            "name": "Development",
            "status": "developing",
            "doi": False,
            "description": (
                "Author evolves the work through refinements, "
                "extensions, and connections. Version history builds. "
                "Still no DOI — work is in active development."
            ),
        },
        {
            "stage": 3,
            "name": "Review Request",
            "status": "developing",
            "doi": False,
            "description": (
                "Author requests expert review. The node must have: "
                "(a) at least 2 connections to other structures, "
                "(b) a description of at least 100 characters, "
                "(c) at least one evolution beyond initial creation. "
                "These gates prevent premature review requests."
            ),
        },
        {
            "stage": 4,
            "name": "Expert Evaluation",
            "status": "developing",
            "doi": False,
            "description": (
                "Reviewer evaluates rigor, novelty, and completeness. "
                "Four possible verdicts: Validated, Needs Revision, "
                "Novel, Not Ready. If 'Needs Revision' → author "
                "revises and resubmits. If 'Not Ready' → author "
                "continues developing."
            ),
        },
        {
            "stage": 5,
            "name": "Stabilization",
            "status": "stable",
            "doi": True,
            "description": (
                "Once validated or confirmed as novel, the node "
                "advances to 'stable' status. A DOI is issued via "
                "Zenodo. The DOI metadata includes: title, creator, "
                "version, field, institution, review verdict, and "
                "reviewer identity. The review itself becomes part "
                "of the DOI record."
            ),
        },
        {
            "stage": 6,
            "name": "Canonization",
            "status": "canonical",
            "doi": True,
            "description": (
                "A Field Founder can elevate a stable node to "
                "canonical status — marking it as authoritative "
                "within the field. Canonical nodes receive an "
                "updated DOI version. Canonization requires at "
                "least two completed reviews from different "
                "institutions."
            ),
        },
    ],

    "doi_metadata_spec": {
        "required_fields": [
            "title",
            "creators (with ORCID if available)",
            "description",
            "node_type",
            "version_number",
            "field_name",
            "keywords / tags",
            "created_date",
            "review_verdict",
            "reviewer_name",
            "reviewer_institution",
        ],
        "optional_fields": [
            "institution_affiliation",
            "related_identifiers (derives_from DOIs)",
            "license",
            "language",
        ],
        "zenodo_mapping": {
            "upload_type": "other",
            "publication_type": "workingpaper (for stable) | report (for canonical)",
            "access_right": "open",
            "communities": ["noderail"],
        },
    },

    "review_gates_summary": {
        "stable_requires": "At least 1 completed review with verdict 'validated' or 'novel'",
        "canonical_requires": "At least 2 completed reviews from different institutions",
        "doi_requires": "Node at 'stable' or 'canonical' status",
        "version_doi_requires": "Major version bump on a DOI-bearing node",
    },

    "revenue_connection": (
        "DOI issuance is a revenue touchpoint: "
        "(1) Free tier: 3 DOIs per year per individual; "
        "(2) Institutional tier: unlimited DOIs included in subscription; "
        "(3) Premium individual: unlimited DOIs for $X/month. "
        "This creates natural upgrade pressure as researchers publish more."
    ),
}


# ===================================================================
# FIRESTORE SECURITY RULES (outline)
# ===================================================================

SECURITY_RULES_OUTLINE = """
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Nodes: anyone can read public nodes, only contributors+ can create
    match /nodes/{nodeId} {
      allow read: if resource.data.is_public == true || request.auth != null;
      allow create: if request.auth != null && getUserRole() in ['contributor', 'field_founder'];
      allow update: if request.auth.uid == resource.data.created_by;
    }

    // Edges: same as nodes
    match /edges/{edgeId} {
      allow read: if true;
      allow create: if request.auth != null && getUserRole() in ['contributor', 'field_founder'];
    }

    // Reviews: reviewers can complete, anyone authenticated can request
    match /reviews/{reviewId} {
      allow read: if true;
      allow create: if request.auth != null;
      allow update: if request.auth.uid == resource.data.reviewer_id;
    }

    // Institutions: admins manage, anyone can read
    match /institutions/{instId} {
      allow read: if true;
      allow write: if request.auth.uid in resource.data.admin_ids;
    }

    // Users: own profile only
    match /users/{userId} {
      allow read: if true;
      allow write: if request.auth.uid == userId;
    }
  }
}
"""


# ===================================================================
# MAPPING: STREAMLIT PROTOTYPE → FIREBASE
# ===================================================================

MIGRATION_NOTES = {
    "data_export": (
        "Use the JSON export from the Publish page to generate "
        "Firestore-compatible documents. The export format maps "
        "directly to the collections above."
    ),
    "auth": (
        "Replace the prototype's 'created_by: author' with "
        "Firebase Auth UIDs. Use Google Sign-In or email/password."
    ),
    "storage": (
        "Replace NodeRailStore (JSON file) with Firestore client. "
        "Each method maps to a Firestore query. get_all_nodes() "
        "becomes db.collection('nodes').get(), etc."
    ),
    "realtime": (
        "Firestore supports real-time listeners. The graph view "
        "can update live as collaborators add nodes and edges."
    ),
    "search": (
        "Add Algolia or Firestore composite indexes for full-text "
        "search across node titles, descriptions, and tags."
    ),
}
