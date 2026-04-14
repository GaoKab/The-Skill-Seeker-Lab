"""
NodeRail Pricing Tiers (v2)

Strategic reference document. Not executable code.

Core principle:
    People don't pay for storage.
    They pay when their work becomes too valuable to risk losing
    or misrepresenting.

Primary conversion drivers:
    - Continuity (work doesn't reset)
    - Governance (validation + credibility)
    - Visibility (institutional insight)

DOIs remain a credibility layer, not the main conversion lever.

Comparable pricing research:
    - Notion: Free, Plus $10/mo, Business $18/mo, Enterprise custom
    - Obsidian: Free, $50/yr (sync), $50/yr (publish)
    - Roam Research: $15/mo (Pro), $500/5yr (Believer)
    - Overleaf: Free, $12/mo (Standard), $19/mo (Pro), institutional ~$4K+/yr
    - Figshare for Institutions: ~$5K-50K+/yr
    - JSTOR: Institutional ~$2K-200K+/yr
    - Elsevier ScienceDirect: Institutional ~$50K-2M+/yr
    - GitHub: Free, Pro $4/mo, Team $4/user/mo, Enterprise $21/user/mo
"""


# ===================================================================
# FREE TIER
# ===================================================================

FREE_TIER = {
    "name": "Free",
    "target": "Individual researchers, graduate students, independent thinkers",
    "price": "$0/month",
    "trigger": "Exploration and early structure",

    "includes": [
        "Unlimited nodes (concepts, frameworks, measurements, etc.)",
        "Unlimited edges (typed relationships)",
        "Unlimited version history and lineage tracking",
        "Full graph visualization",
        "Export to JSON and Markdown",
        "3 DOI issuances per year",
        "Request up to 5 expert reviews per year",
        "Public profile with ORCID integration",
        "Community support",
    ],

    "limits": [
        "3 DOIs per year",
        "5 review requests per year",
        "No private/draft-only structures",
        "No institutional features",
        "No API access",
        "NodeRail branding on exported artifacts",
    ],

    "rationale": (
        "The free tier must be genuinely useful, not a crippled trial. "
        "A researcher should be able to build a full body of work here. "
        "The goal is to build graph density and habit. The more knowledge "
        "published at the free level, the more valuable the platform "
        "becomes for everyone."
    ),
}


# ===================================================================
# PRO TIER
# ===================================================================

PRO_TIER = {
    "name": "Pro",
    "target": "Active researchers, field founders, serious builders",
    "price": "$12/month ($120/year) or $15/month billed monthly",
    "trigger": "I rely on this for my work",

    "includes": [
        "Everything in Free",
        "Unlimited DOI issuances",
        "Unlimited review requests",
        "Private/draft structures (visible only to author until published)",
        "Priority review matching",
        "Advanced graph analytics (hub detection, gap analysis, lineage depth)",
        "Custom export templates (branded Markdown, HTML, PDF)",
        "Clean exports without NodeRail branding",
        "Personal API key (read-only, own content, 1,000 requests/day)",
        "Email support with 48-hour response",
    ],

    "limits": [
        "Single user (no team features)",
        "API limited to own content",
        "No institutional admin",
    ],

    "rationale": (
        "Priced at Overleaf Standard level, below Roam. Affordable for "
        "a working academic or funded researcher. $120/year is easy to "
        "justify on a research budget. The key upgrade trigger is not "
        "DOIs — it's private drafts and the feeling of 'I rely on this "
        "for my work.' Unlimited DOIs and reviews reinforce commitment."
    ),
}


# ===================================================================
# INSTITUTIONAL TIERS
# ===================================================================

INSTITUTIONAL_TIER = {
    "name": "Institutional",
    "target": "Universities, research labs, think tanks, corporate R&D",

    "sub_tiers": {

        "lab": {
            "name": "Lab",
            "target": "Small research labs, working groups (up to 15 members)",
            "price": "$2,400/year ($200/month)",
            "seats": "Up to 15 members",
            "trigger": "We need shared thinking, not shared docs",

            "includes": [
                "Everything in Pro for all members",
                "Institutional profile and branding",
                "Shared institutional graph view",
                "Member management (admin panel)",
                "Unlimited DOIs for all members",
                "Internal review workflows",
                "Knowledge continuity across member turnover",
                "Priority email support with 24-hour response",
            ],

            "rationale": (
                "Payable from a single PI's discretionary budget. "
                "$200/month for 15 people is $13.33/person/month. "
                "The real trigger is team knowledge continuity — when "
                "a grad student leaves, their work doesn't disappear."
            ),
        },

        "department": {
            "name": "Department",
            "target": "Academic departments, research centers (up to 75 members)",
            "price": "$9,000/year ($750/month)",
            "seats": "Up to 75 members",
            "trigger": "We need to understand and preserve institutional knowledge",

            "includes": [
                "Everything in Lab",
                "Up to 75 members",
                "Cross-lab graph analytics (how department work connects)",
                "Department-level DOI analytics and reporting",
                "Custom review workflows (multi-reviewer, sequential)",
                "SSO integration (SAML 2.0)",
                "Dedicated onboarding session (2 hours)",
                "API access for institutional content (10,000 requests/day)",
                "Dedicated support contact",
            ],

            "rationale": (
                "Comparable to a single journal subscription. SSO is "
                "a must-have for IT approval. Cross-lab analytics is "
                "the unique value: department chairs can see how their "
                "faculty's work interconnects."
            ),
        },

        "university": {
            "name": "University",
            "target": "University-wide deployment, large research institutions",
            "price": "$25,000 - $75,000/year (based on FTE researchers)",
            "seats": "Unlimited",
            "trigger": "We need knowledge visibility and governance at scale",

            "includes": [
                "Everything in Department",
                "Unlimited members",
                "University-wide knowledge graph",
                "Multi-department admin hierarchies",
                "Custom data residency options",
                "Full API access (100,000 requests/day)",
                "Custom integration support (LMS, repository, CRIS)",
                "Dedicated customer success manager",
                "Quarterly business reviews",
                "Volume DOI pricing",
                "Uptime SLA (99.9%)",
            ],

            "rationale": (
                "Competitive with Figshare/Dimensions institutional "
                "pricing. A fraction of journal bundles. The unique "
                "proposition: no other tool shows a university how its "
                "entire intellectual output connects and evolves."
            ),
        },
    },
}


# ===================================================================
# AI API TIER
# ===================================================================

AI_API_TIER = {
    "name": "AI API",
    "target": "AI developers, LLM applications, RAG systems",
    "price": "Usage-based",
    "trigger": "We need reliable, attributed knowledge for AI",

    "rate_card": {
        "free_exploration": {
            "price": "$0",
            "limits": "100 requests/day, public content only",
            "target": "Developers evaluating the API",
        },
        "starter": {
            "price": "$49/month",
            "limits": "10,000 requests/day, full public content",
            "target": "Small AI applications, research tools",
        },
        "growth": {
            "price": "$199/month",
            "limits": "100,000 requests/day, graph traversal queries",
            "target": "Production AI applications, RAG pipelines",
        },
        "enterprise": {
            "price": "Custom",
            "limits": "Unlimited, dedicated endpoint, training data license negotiable",
            "target": "Large AI companies, foundational model providers",
        },
    },

    "api_features": [
        "Retrieve structures with full metadata and provenance",
        "Query by type, status, field, institution, or tag",
        "Traverse relationships (N-hop graph queries)",
        "Retrieve version history and evolution lineage",
        "Retrieve reviews and validation status",
        "Full-text search",
        "Structured JSON responses with DOI metadata",
    ],

    "rationale": (
        "No other platform offers an API to structured, expert-reviewed, "
        "DOI-backed knowledge objects with typed relationships and "
        "provenance. This is qualitatively different from scraping "
        "Wikipedia or accessing arXiv. The AI API is NodeRail's "
        "long-term strategic moat — it becomes more valuable as the "
        "graph grows."
    ),
}


# ===================================================================
# ENTERPRISE TIER
# ===================================================================

ENTERPRISE_TIER = {
    "name": "Enterprise",
    "target": "Large corporations, government, pharma R&D, defense research",
    "price": "Custom ($50,000 - $200,000+/year)",
    "trigger": "We need isolation, compliance, and custom governance",

    "includes": [
        "Everything in University",
        "Private instance (isolated infrastructure)",
        "Custom data residency and sovereignty compliance",
        "On-premise deployment option",
        "Custom node types and relationship types",
        "Custom review workflows and compliance gates",
        "Advanced audit logging",
        "SCIM provisioning",
        "SSO with custom identity providers",
        "Full AI API with dedicated endpoint",
        "Training data license (negotiated)",
        "Custom SLA (up to 99.99%)",
        "24/7 support with 4-hour response",
        "Dedicated implementation team",
        "Source code escrow",
    ],

    "rationale": (
        "Enterprise pricing is relationship-based. Pharma needs audit "
        "trails. Defense needs air-gapped deployments. Consulting firms "
        "need custom ontologies. The price reflects customization and "
        "support depth."
    ),
}


# ===================================================================
# PRICING SUMMARY
# ===================================================================

PRICING_SUMMARY = {
    "header": ["Tier", "Price", "Trigger", "Key Value"],
    "rows": [
        ("Free", "$0", "Exploration", "Full graph, basic publishing"),
        ("Pro", "$12/mo", "I rely on this", "Private drafts, unlimited validation"),
        ("Lab", "$200/mo", "Shared thinking", "Team continuity, shared graph"),
        ("Department", "$750/mo", "Institutional knowledge", "Cross-lab insight, SSO"),
        ("University", "$25-75K/yr", "Visibility at scale", "Full institutional graph"),
        ("AI API", "$0-199/mo+", "Trusted AI access", "Structured knowledge API"),
        ("Enterprise", "Custom", "Compliance + isolation", "Private instance"),
    ],
}


# ===================================================================
# STRATEGIC NOTES
# ===================================================================

STRATEGIC_NOTES = {
    "primary_conversion_drivers": (
        "Continuity + governance + visibility — not DOIs alone. "
        "The upgrade trigger is 'I rely on this for my work' (Pro) "
        "and 'we need shared thinking, not shared docs' (Lab). "
        "DOIs remain a credibility layer but are not the main lever."
    ),

    "doi_role": (
        "DOIs are still capped on Free (3/year) to create natural "
        "upgrade pressure. But the pitch should be about continuity "
        "and governance, not about DOI limits. DOIs are the proof "
        "that your work matters, not the reason you upgrade."
    ),

    "institutional_land_and_expand": (
        "Bottom-up: researcher starts Free → upgrades to Pro → "
        "champions Lab for their group. Top-down: Department and "
        "University sold to administrators once bottom-up adoption "
        "exists. Every institutional deal starts with a free pilot."
    ),

    "api_as_moat": (
        "More researchers → more validated knowledge → more API value → "
        "more revenue → more funded reviews → more researchers. "
        "This flywheel is NodeRail's long-term competitive moat."
    ),

    "pricing_principles": [
        "Never punish free users — free tier should feel complete.",
        "Price on value (continuity, governance, visibility), not features everyone needs.",
        "Institutional pricing = research infrastructure, not 'another SaaS tool.'",
        "AI API pricing = transparent and usage-based.",
        "Enterprise pricing = custom because enterprise needs are custom.",
    ],
}
