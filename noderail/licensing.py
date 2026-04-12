"""
NodeRail Licensing Strategy

Decision: Continuity Standard = Open | Platform = Proprietary

This reflects the strategic balance between trust (academics prefer
open standards) and defensibility (the platform is the business).
"""

LICENSING_STRATEGY = {
    "decision": "Continuity Standard = Open. Platform = Proprietary.",

    "open_components": {
        "continuity_standard": {
            "license": "Creative Commons Attribution 4.0 (CC BY 4.0)",
            "rationale": (
                "The Continuity Standard defines how knowledge should be "
                "structured, versioned, and governed. Making it open "
                "builds trust with academics, enables adoption by other "
                "platforms, and positions NodeRail as the reference "
                "implementation. If others build on the standard, "
                "NodeRail benefits from ecosystem growth. CC BY 4.0 "
                "requires attribution, so NodeRail is always credited."
            ),
        },
        "data_model_spec": {
            "license": "Creative Commons Attribution 4.0 (CC BY 4.0)",
            "rationale": (
                "The node types, relationship types, evolution types, "
                "and status levels are part of the standard. Publishing "
                "them openly lets other tools interoperate. This creates "
                "a network effect around the vocabulary itself."
            ),
        },
        "export_format": {
            "license": "Creative Commons Attribution 4.0 (CC BY 4.0)",
            "rationale": (
                "The JSON export format should be open so that users "
                "are never locked in. Data portability builds trust "
                "and is increasingly required by regulation."
            ),
        },
    },

    "proprietary_components": {
        "platform_code": {
            "what": "The NodeRail web application, API, and infrastructure",
            "rationale": (
                "This is the product. The code that runs noderail.web.app, "
                "the review workflow engine, the graph analytics, the "
                "institutional management — all proprietary. This is "
                "what competitors would need to rebuild, and it's "
                "protected by copyright."
            ),
        },
        "review_system": {
            "what": "The expert review pipeline and matching algorithm",
            "rationale": (
                "The structured review process — how reviewers are matched, "
                "how evaluations are structured, how reviews gate DOI "
                "issuance — is a competitive advantage. Open-sourcing "
                "this would hand competitors the governance layer."
            ),
        },
        "insights_engine": {
            "what": "Gap detection, structural analysis, graph intelligence",
            "rationale": (
                "The system that surfaces unmeasured concepts, unsupported "
                "inquiries, stale structures, and knowledge hubs is a "
                "differentiator. This is the 'thinking amplifier' layer."
            ),
        },
        "ai_api": {
            "what": "The AI attribution API and access control",
            "rationale": (
                "The API that serves structured knowledge to AI systems "
                "with attribution and provenance is a primary revenue "
                "source. The implementation, rate limiting, and access "
                "control are proprietary."
            ),
        },
    },

    "trademark": {
        "name": "NodeRail",
        "status": "Use NodeRail™ on all materials until formal registration",
        "action_items": [
            "Add ™ to website footer and all published materials immediately (free)",
            "File USPTO trademark application when funds allow (~$250-350)",
            "Register in relevant international markets as budget permits",
        ],
    },

    "summary": (
        "Open the standard, close the platform. This gives NodeRail "
        "the trust of open-source and the defensibility of proprietary "
        "software. The standard grows the ecosystem. The platform "
        "captures the value. Competitors can build on the Continuity "
        "Standard — but they'd be building toward NodeRail's vocabulary, "
        "not away from it."
    ),
}
