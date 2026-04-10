"""
NodeRail Pricing Tiers

Strategic reference document. Not executable code.
Defines pricing structure with per-tier features, price points,
and strategic rationale.

Comparable pricing research:
    - Notion: Free (limited), Plus $10/mo, Business $18/mo, Enterprise custom
    - Obsidian: Free (personal), $50/yr (sync), $50/yr (publish)
    - Roam Research: $15/mo (Pro), $500/5yr (Believer)
    - Overleaf (academic LaTeX): Free, $12/mo (Standard), $19/mo (Pro),
      institutional plans from ~$4,000/yr
    - ResearchGate: Free (ad-supported)
    - Zenodo: Free (CERN-funded)
    - Digital Science Dimensions: Institutional pricing ~$10K-50K+/yr
    - JSTOR: Institutional pricing ~$2K-200K+/yr depending on institution size
    - Figshare for Institutions: ~$5K-50K+/yr
    - Elsevier ScienceDirect: Institutional ~$50K-2M+/yr
    - GitHub: Free, Pro $4/mo, Team $4/user/mo, Enterprise $21/user/mo

Pricing philosophy:
    NodeRail sits between consumer knowledge tools ($0-15/mo) and
    institutional research infrastructure ($5K-200K+/yr). Individual
    pricing should be accessible to graduate students. Institutional
    pricing should be justifiable as research infrastructure, not
    software licensing. The AI API is a distinct revenue line priced
    on usage, not seats.
"""


# ===================================================================
# FREE TIER — Individual
# ===================================================================

FREE_TIER = {
    "name": "Free",
    "target": "Individual researchers, graduate students, independent thinkers",
    "price": "$0/month",

    "includes": [
        "Unlimited nodes (concepts, frameworks, measurements, etc.)",
        "Unlimited edges (typed relationships between structures)",
        "Unlimited version history and lineage tracking",
        "Full graph visualization",
        "Export to JSON and Markdown",
        "3 DOI issuances per year",
        "Request up to 5 expert reviews per year",
        "Public profile with ORCID integration",
        "Community support",
    ],

    "limits": [
        "3 DOIs per year (hard cap)",
        "5 review requests per year",
        "No institutional affiliation features",
        "No API access",
        "No private/draft-only structures (all content visible at exploratory+)",
        "NodeRail branding on exported artifacts",
    ],

    "rationale": (
        "The free tier must be genuinely useful, not a crippled trial. "
        "A researcher should be able to build a full body of work on "
        "the free tier. The DOI cap creates natural upgrade pressure: "
        "once someone has 3 validated structures per year, they are "
        "serious enough to pay. Unlimited nodes and edges ensure the "
        "knowledge graph is rich even at the free level, which makes "
        "the platform more valuable for everyone."
    ),
}


# ===================================================================
# PRO TIER — Individual, Paid
# ===================================================================

PRO_TIER = {
    "name": "Pro",
    "target": "Active researchers, field founders, prolific publishers",
    "price": "$12/month (billed annually at $120/year) or $15/month billed monthly",

    "includes": [
        "Everything in Free tier",
        "Unlimited DOI issuances",
        "Unlimited review requests",
        "Private/draft structures (visible only to author until published)",
        "Priority review matching (faster reviewer assignment)",
        "Advanced graph analytics (hub detection, gap analysis, lineage depth)",
        "Custom export templates (branded Markdown, HTML, PDF)",
        "Clean exports without NodeRail branding",
        "Personal API key (read-only, for own content, 1,000 requests/day)",
        "Email support with 48-hour response",
    ],

    "limits": [
        "Single user (no team features)",
        "API access limited to own content",
        "No institutional admin capabilities",
    ],

    "rationale": (
        "Priced at the level of Overleaf Standard or slightly below "
        "Roam Research — affordable for a working academic or funded "
        "researcher. The key upgrades are unlimited DOIs (the primary "
        "driver), private drafts (important for pre-publication work), "
        "and the personal API key. Annual billing discount encourages "
        "commitment. $120/year is easy to justify on a research budget "
        "or as a personal professional expense."
    ),
}


# ===================================================================
# INSTITUTIONAL TIER — With Sub-Tiers
# ===================================================================

INSTITUTIONAL_TIER = {
    "name": "Institutional",
    "target": "Universities, research labs, think tanks, corporate R&D",

    "sub_tiers": {

        "small_lab": {
            "name": "Lab",
            "target": "Small research labs, working groups (up to 15 members)",
            "price": "$2,400/year ($200/month)",
            "seats": "Up to 15 members",

            "includes": [
                "Everything in Pro tier for all members",
                "Institutional profile and branding",
                "Shared institutional graph view",
                "Member management (admin panel)",
                "Unlimited DOIs for all members",
                "Unlimited review requests",
                "Institutional usage reports (aggregate)",
                "Ability to designate internal reviewers",
                "Priority email support with 24-hour response",
            ],

            "rationale": (
                "Priced to be payable from a single PI's discretionary "
                "budget or a small grant line item. $200/month for a "
                "lab of 15 is $13.33/person/month — comparable to Pro "
                "tier per person but with collaboration and admin "
                "features. Most small labs will have 5-10 active users, "
                "making effective per-user cost even lower."
            ),
        },

        "department": {
            "name": "Department",
            "target": "Academic departments, research centers (up to 75 members)",
            "price": "$9,000/year ($750/month)",
            "seats": "Up to 75 members",

            "includes": [
                "Everything in Lab tier",
                "Up to 75 members",
                "Cross-lab graph analytics (see how department work connects)",
                "Department-level DOI analytics and reporting",
                "Custom review workflows (multi-reviewer, sequential review)",
                "SSO integration (SAML 2.0)",
                "Dedicated onboarding session (2 hours)",
                "API access for institutional content (10,000 requests/day)",
                "Dedicated support contact",
            ],

            "rationale": (
                "Priced in the range of Figshare institutional pricing "
                "and far below JSTOR or Elsevier bundles. $9K/year is "
                "a line item in a department budget, comparable to a "
                "single journal subscription. SSO is a must-have at "
                "this level — IT departments will not approve tools "
                "without it. Cross-lab analytics are a unique value "
                "proposition: department chairs can see how their "
                "faculty's work interconnects."
            ),
        },

        "university": {
            "name": "University",
            "target": "University-wide deployment, large research institutions",
            "price": "$25,000 - $75,000/year (based on FTE researchers)",
            "seats": "Unlimited",

            "includes": [
                "Everything in Department tier",
                "Unlimited members",
                "University-wide knowledge graph",
                "Multi-department structure with separate admin hierarchies",
                "Custom data residency options (EU, specific regions)",
                "Full API access for institutional content (100,000 requests/day)",
                "Custom integration support (LMS, repository, CRIS systems)",
                "Dedicated customer success manager",
                "Quarterly business reviews",
                "Volume DOI pricing (reduced per-DOI cost for high volume)",
                "Early access to new features",
                "Uptime SLA (99.9%)",
            ],

            "rationale": (
                "University pricing is negotiated based on institutional "
                "size (FTE researchers, not total enrollment). The range "
                "$25K-75K is competitive with research infrastructure "
                "tools like Figshare for Institutions or Dimensions, "
                "and is a fraction of what universities pay for journal "
                "bundles. The value proposition is unique: no other "
                "tool shows a university how its entire intellectual "
                "output connects across departments and evolves over "
                "time. Data residency and custom integrations are "
                "table stakes at this level."
            ),
        },
    },
}


# ===================================================================
# AI API TIER — Usage-Based
# ===================================================================

AI_API_TIER = {
    "name": "AI API",
    "target": "AI developers, LLM applications, research tools, RAG systems",
    "price": "Usage-based (see rate card below)",

    "rate_card": {
        "free_exploration": {
            "price": "$0",
            "limits": "100 requests/day, public content only, attribution required",
            "target": "Developers evaluating the API",
        },
        "starter": {
            "price": "$49/month",
            "limits": "10,000 requests/day, full public content, structured responses",
            "target": "Small AI applications, academic research tools",
        },
        "growth": {
            "price": "$199/month",
            "limits": "100,000 requests/day, full content including graph traversal queries",
            "target": "Production AI applications, RAG pipelines",
        },
        "enterprise": {
            "price": "Custom pricing",
            "limits": "Unlimited requests, dedicated endpoint, bulk export, training data license negotiable",
            "target": "Large AI companies, foundational model providers",
        },
    },

    "api_features": [
        "Retrieve individual structures with full metadata",
        "Query by type, status, field, institution, or tag",
        "Traverse relationships (get all structures connected to X)",
        "Retrieve version history and evolution lineage",
        "Retrieve reviews and validation status",
        "Graph neighborhood queries (N-hop traversal)",
        "Full-text search across titles and descriptions",
        "Structured JSON responses with DOI and provenance metadata",
    ],

    "terms": [
        "Attribution required in all tiers",
        "Training data usage requires Enterprise tier and separate agreement",
        "Author opt-out respected (opted-out content excluded from API)",
        "Rate limits enforced per API key",
        "No resale of raw API access",
    ],

    "rationale": (
        "The AI API is NodeRail's most distinctive revenue line and "
        "its long-term strategic asset. No other platform offers an "
        "API to structured, expert-reviewed, DOI-backed knowledge "
        "objects with typed relationships and provenance. This is "
        "qualitatively different from scraping Wikipedia or accessing "
        "arXiv — NodeRail content is structured, validated, and "
        "interconnected. Pricing is usage-based to align with how AI "
        "companies buy infrastructure. The training data license at "
        "Enterprise tier is a high-margin upsell that protects authors "
        "while enabling legitimate use. Revenue sharing with authors "
        "whose content is accessed creates a virtuous cycle."
    ),
}


# ===================================================================
# ENTERPRISE TIER
# ===================================================================

ENTERPRISE_TIER = {
    "name": "Enterprise",
    "target": (
        "Large corporations, government agencies, pharmaceutical R&D, "
        "defense research organizations, major consulting firms"
    ),
    "price": "Custom pricing (typically $50,000 - $200,000+/year)",

    "includes": [
        "Everything in University tier",
        "Private instance option (isolated Firestore, dedicated infrastructure)",
        "Custom data residency and sovereignty compliance",
        "On-premise deployment option (for classified/regulated environments)",
        "Custom node types and relationship types (extend the ontology)",
        "Custom review workflows and compliance gates",
        "Advanced audit logging and compliance reporting",
        "SCIM provisioning for user lifecycle management",
        "SSO with custom identity providers",
        "Full AI API access with dedicated endpoint",
        "Training data license (negotiated separately)",
        "Custom SLA (up to 99.99% uptime)",
        "24/7 support with 4-hour response time",
        "Dedicated implementation team for onboarding",
        "Annual roadmap input session",
        "Source code escrow (for business continuity)",
    ],

    "rationale": (
        "Enterprise pricing is relationship-based and highly variable. "
        "The key differentiator at this level is isolation, compliance, "
        "and customization. Pharma companies need audit trails for "
        "research integrity. Defense organizations need air-gapped "
        "deployments. Consulting firms need custom ontologies for "
        "their proprietary frameworks. The price range reflects the "
        "depth of customization and support required. Source code "
        "escrow and custom SLAs are standard requests at this level "
        "and should be offered proactively."
    ),
}


# ===================================================================
# PRICING SUMMARY TABLE
# ===================================================================

PRICING_SUMMARY = {
    "header": ["Tier", "Price", "DOIs", "Seats", "API", "Key Feature"],
    "rows": [
        ("Free", "$0", "3/year", "1", "No", "Full graph, basic publishing"),
        ("Pro", "$12/mo", "Unlimited", "1", "Own content", "Private drafts, priority review"),
        ("Lab", "$200/mo", "Unlimited", "15", "No", "Team graph, member management"),
        ("Department", "$750/mo", "Unlimited", "75", "10K req/day", "SSO, cross-lab analytics"),
        ("University", "$25-75K/yr", "Unlimited", "Unlimited", "100K req/day", "Full institutional graph"),
        ("AI API", "$0-199/mo+", "N/A", "N/A", "Core product", "Structured knowledge access"),
        ("Enterprise", "Custom", "Unlimited", "Unlimited", "Dedicated", "Private instance, compliance"),
    ],
}


# ===================================================================
# STRATEGIC NOTES
# ===================================================================

STRATEGIC_NOTES = {
    "doi_as_upgrade_driver": (
        "The 3 DOI/year cap on the free tier is the primary conversion "
        "mechanism. A researcher who hits this cap has demonstrated "
        "that they are producing validated, citable work — exactly "
        "the user who will pay $12/month without hesitation. The cap "
        "should feel generous enough that casual users never hit it, "
        "but tight enough that serious researchers upgrade within "
        "their first year."
    ),

    "institutional_land_and_expand": (
        "The institutional sales motion is bottom-up: a single "
        "researcher starts on Free, upgrades to Pro, then champions "
        "the Lab tier when their group wants shared infrastructure. "
        "Department and University tiers are sold top-down to "
        "administrators once there is bottom-up adoption. Every "
        "institutional deal should start with a free pilot for one "
        "lab."
    ),

    "api_as_moat": (
        "The AI API becomes more valuable as the knowledge graph "
        "grows. This is a network effect: more researchers publishing "
        "validated work means more structured knowledge available "
        "through the API, which attracts more AI customers, which "
        "generates revenue that can be shared with authors, which "
        "attracts more researchers. This flywheel is NodeRail's "
        "long-term competitive moat."
    ),

    "pricing_principles": [
        "Never punish free users — the free tier should feel complete, not crippled.",
        "Price on value (DOIs, validation, permanence), not on features everyone needs (nodes, edges, graph).",
        "Institutional pricing should be justifiable as research infrastructure, not 'another SaaS tool.'",
        "AI API pricing should be transparent and usage-based — no 'contact sales' for standard tiers.",
        "Enterprise pricing is custom because enterprise needs are custom — this is honest, not evasive.",
    ],

    "competitive_price_anchors": {
        "vs_overleaf": "Pro at $12/mo is comparable to Overleaf Standard ($12/mo) but provides DOIs, review, and lineage — not just LaTeX editing.",
        "vs_roam": "Pro at $12/mo undercuts Roam ($15/mo) while offering a publication path Roam lacks entirely.",
        "vs_figshare_institutional": "University tier at $25-75K competes with Figshare for Institutions but offers structured knowledge, not just file storage.",
        "vs_journal_subscriptions": "A university paying $50K/year for NodeRail is paying less than a single Elsevier journal bundle while getting a tool that actually structures and connects research output.",
        "vs_github_enterprise": "Enterprise at $50-200K is in the range of GitHub Enterprise for large organizations, but NodeRail serves a fundamentally different purpose — knowledge, not code.",
    },
}
