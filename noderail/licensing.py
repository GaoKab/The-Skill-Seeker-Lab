"""
NodeRail Licensing Strategy (v2)

Decision: Continuity Standard = Open | Platform = Proprietary

Infrastructure requires two things:
- Openness where trust, portability, and ecosystem growth matter
- Control where governance, validation, and intelligence create value
"""

LICENSING_STRATEGY = {
    "decision": "The Continuity Standard is open. The NodeRail platform is proprietary.",

    "principle": (
        "NodeRail is building knowledge infrastructure. Infrastructure "
        "requires openness where trust, portability, and ecosystem growth "
        "matter — and control where governance, validation, and intelligence "
        "create value."
    ),

    # =================================================================
    # OPEN LAYER
    # =================================================================

    "open_components": {
        "continuity_standard": {
            "license": "Creative Commons Attribution 4.0 (CC BY 4.0)",
            "what": (
                "The knowledge structure vocabulary: concepts, frameworks, "
                "measurements, relationships, evolution types, status levels. "
                "The specification that defines how knowledge should be "
                "structured, versioned, and governed."
            ),
            "rationale": (
                "Making the standard open builds academic and institutional "
                "trust, enables ecosystem adoption, prevents lock-in, and "
                "positions NodeRail as the reference implementation. If "
                "others build on the standard, they build toward NodeRail's "
                "vocabulary, not away from it."
            ),
        },
        "data_model_spec": {
            "license": "Creative Commons Attribution 4.0 (CC BY 4.0)",
            "what": (
                "The formal specification of node types, relationship types, "
                "evolution types, and status levels. The shared vocabulary "
                "that makes interoperability possible."
            ),
            "rationale": (
                "Publishing the data model openly lets other tools "
                "interoperate. This creates a network effect around the "
                "vocabulary itself."
            ),
        },
        "export_format": {
            "license": "Creative Commons Attribution 4.0 (CC BY 4.0)",
            "what": (
                "The JSON export format and structured schema. The format "
                "users receive when they export their data."
            ),
            "rationale": (
                "Data portability builds trust and is increasingly required "
                "by regulation. Users must never feel locked in."
            ),
        },
    },

    # =================================================================
    # PROPRIETARY LAYER
    # =================================================================

    "proprietary_components": {
        "platform_code": {
            "what": (
                "The NodeRail web application, API, and infrastructure — "
                "everything that runs noderail.web.app."
            ),
            "rationale": (
                "This is the product. The code, the review workflow engine, "
                "the graph analytics, the institutional management — all "
                "proprietary. This is where trust is enforced, quality is "
                "maintained, intelligence is generated, and value is captured."
            ),
        },
        "review_system": {
            "what": (
                "The expert review pipeline: how reviewers are matched, "
                "how evaluations are structured, how reviews gate DOI "
                "issuance and canon advancement."
            ),
            "rationale": (
                "The governance layer is a competitive advantage. "
                "Open-sourcing it would hand competitors the trust engine."
            ),
        },
        "insights_engine": {
            "what": (
                "Gap detection, structural analysis, graph intelligence — "
                "the system that surfaces what's missing, what's stuck, "
                "and what's ready to advance."
            ),
            "rationale": (
                "This is the 'thinking amplifier' layer. It's what makes "
                "NodeRail active rather than passive."
            ),
        },
        "ai_api": {
            "what": (
                "The AI attribution API: structured access to validated "
                "knowledge with provenance, rate limiting, and access control."
            ),
            "rationale": (
                "Primary long-term revenue source. The implementation, "
                "access control, and attribution enforcement are proprietary."
            ),
        },
    },

    # =================================================================
    # STANDARD GOVERNANCE (NEW)
    # =================================================================

    "standard_governance": {
        "principle": (
            "NodeRail maintains the canonical Continuity Standard. "
            "The standard evolves through a governed process, not "
            "through uncontrolled forks."
        ),
        "rules": [
            {
                "rule": "All changes to the standard are versioned",
                "detail": (
                    "Every update to the Continuity Standard receives a "
                    "version number and a changelog. Breaking changes require "
                    "a major version bump."
                ),
            },
            {
                "rule": "Extensions are allowed but cannot claim canonical status",
                "detail": (
                    "Anyone can extend the vocabulary (add new node types, "
                    "relationship types, etc.) for their own use. But only "
                    "NodeRail-governed updates to the standard are canonical. "
                    "Extensions must be clearly marked as non-standard."
                ),
            },
            {
                "rule": "Compatibility rules are defined",
                "detail": (
                    "Tools that claim compatibility with the Continuity "
                    "Standard must support the full canonical vocabulary. "
                    "Extensions are optional. This prevents fragmentation."
                ),
            },
            {
                "rule": "NodeRail acts as standard steward",
                "detail": (
                    "NodeRail convenes an advisory process for major standard "
                    "changes. This may evolve into a formal standards body "
                    "as adoption grows. Until then, NodeRail is the steward."
                ),
            },
        ],
    },

    # =================================================================
    # TRADEMARK
    # =================================================================

    "trademark": {
        "name": "NodeRail",
        "status": "Use NodeRail™ on all materials until formal registration",
        "action_items": [
            "Add ™ to website footer and all published materials immediately (free)",
            "File USPTO trademark application when funds allow (~$250-350)",
            "Register in relevant international markets as budget permits",
        ],
    },

    # =================================================================
    # STRATEGIC SUMMARY
    # =================================================================

    "summary": (
        "Open standard → ecosystem growth. "
        "Proprietary platform → value capture. "
        "Standard governance → trust and coherence. "
        "Structured knowledge → AI advantage.\n\n"
        "The standard grows the ecosystem. The platform captures the value. "
        "Competitors can build on the Continuity Standard — but they'd be "
        "building toward NodeRail's vocabulary, not away from it."
    ),
}
