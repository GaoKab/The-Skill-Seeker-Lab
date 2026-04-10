"""
NodeRail Seed Script — Business Model & Revenue Structures

Seeds NodeRail with its own business model as structured knowledge.
The business model is itself a body of thought — with frameworks,
concepts, inquiries, and projects — governed by NodeRail.

Run: python seed_business_model.py
(Run after seed_hcs.py)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from noderail.models import Node, Edge, _now
from noderail.storage import NodeRailStore


def seed():
    store = NodeRailStore()

    # Check that HCS data exists
    if store.stats()["total_nodes"] == 0:
        print("Run seed_hcs.py first.")
        return

    # Get NodeRail project node (already seeded)
    noderail_node = None
    for n in store.get_all_nodes():
        if n.title == "NodeRail":
            noderail_node = n
            break

    if not noderail_node:
        print("NodeRail project node not found. Run seed_hcs.py first.")
        return

    # ===================================================================
    # BUSINESS MODEL FRAMEWORK
    # ===================================================================

    biz_model = Node(
        title="NodeRail Revenue Model",
        description=(
            "A four-layer revenue model for NodeRail as governed knowledge "
            "infrastructure. Revenue flows from: (1) individual contributors "
            "who publish for free, building graph density; (2) institutions "
            "that pay for team workspaces, review infrastructure, and bulk "
            "DOI issuance; (3) AI companies that pay for attributed API "
            "access to governed knowledge; (4) DOI and citation services "
            "as a transaction layer. The model is designed so that the "
            "threat NodeRail was built to counter — AI consuming knowledge "
            "without attribution — becomes the primary revenue source."
        ),
        node_type="framework",
        status="exploratory",
        tags=["business-model", "revenue", "strategy"],
    )
    store.add_node(biz_model)

    # ===================================================================
    # REVENUE LAYER CONCEPTS
    # ===================================================================

    layer_free = Node(
        title="Free Individual Layer",
        description=(
            "Researchers, thinkers, and writers publish structured, "
            "versioned, DOI-backed work on NodeRail for free. This layer "
            "builds graph density — the more knowledge published, the "
            "more valuable the platform becomes to institutions and AI "
            "consumers. Free publishing is not charity; it is the growth "
            "engine."
        ),
        node_type="concept",
        status="developing",
        tags=["business-model", "growth", "individuals"],
    )
    store.add_node(layer_free)

    layer_institutional = Node(
        title="Institutional License Layer",
        description=(
            "Universities, research labs, think tanks, corporate R&D, "
            "and government agencies pay for: team workspaces, private "
            "fields, expert review infrastructure, bulk DOI issuance, "
            "analytics on how their work is cited and extended, and "
            "institutional branding. This is the primary near-term "
            "revenue source — institutions already have budget lines "
            "for research infrastructure and journal subscriptions."
        ),
        node_type="concept",
        status="developing",
        tags=["business-model", "institutions", "revenue"],
    )
    store.add_node(layer_institutional)

    layer_ai_api = Node(
        title="AI Attribution API Layer",
        description=(
            "AI companies pay for API access to governed, attributed "
            "knowledge. When AI systems consume NodeRail content, "
            "they get structured data with provenance, versioning, and "
            "authorship metadata. This is NodeRail's strategic moat: "
            "the very threat it was built to counter (AI stripping "
            "attribution) becomes the revenue engine. As AI regulation "
            "increases, demand for attributed training data grows."
        ),
        node_type="concept",
        status="exploratory",
        tags=["business-model", "AI", "API", "attribution", "revenue"],
    )
    store.add_node(layer_ai_api)

    layer_doi = Node(
        title="DOI & Citation Services Layer",
        description=(
            "Transaction-based revenue from DOI issuance and citation "
            "tracking. While Zenodo provides free DOIs, the value-add "
            "is the structured citation tracking, cross-reference "
            "resolution, and lineage visualization that NodeRail builds "
            "on top. Subscription tiers for unlimited DOIs vs per-issue."
        ),
        node_type="concept",
        status="exploratory",
        tags=["business-model", "DOI", "citation", "revenue"],
    )
    store.add_node(layer_doi)

    # ===================================================================
    # STRATEGIC CONCEPTS
    # ===================================================================

    flywheel = Node(
        title="NodeRail Flywheel",
        description=(
            "The self-reinforcing growth loop: More published knowledge → "
            "more valuable to AI → more API revenue → more funded expert "
            "reviews → more people publish → graph grows → more valuable "
            "to institutions → more institutional subscribers → more "
            "researchers publishing. Each turn of the flywheel increases "
            "density, trust, and revenue simultaneously."
        ),
        node_type="concept",
        status="developing",
        tags=["strategy", "growth", "flywheel"],
    )
    store.add_node(flywheel)

    compliance_positioning = Node(
        title="Compliance Positioning",
        description=(
            "NodeRail's pitch to AI companies is not 'buy our product' — "
            "it is 'solve your compliance problem.' As AI regulation "
            "advances (EU AI Act, potential US legislation), companies "
            "will need to demonstrate provenance for training data. "
            "NodeRail provides the attribution infrastructure that makes "
            "AI knowledge consumption auditable and defensible."
        ),
        node_type="concept",
        status="exploratory",
        tags=["strategy", "compliance", "AI-regulation", "positioning"],
    )
    store.add_node(compliance_positioning)

    reviewer_economics = Node(
        title="Reviewer Economics",
        description=(
            "Expert reviewers on NodeRail get paid for their evaluations. "
            "Revenue sources for reviewer compensation: (1) institutional "
            "subscriptions fund their members' reviews; (2) AI API revenue "
            "subsidizes a review pool for independent researchers; "
            "(3) independent authors pay a small fee for review, kept "
            "accessible through subsidy. Reviewers also earn: permanent "
            "attributed review records, visible expertise profiles, and "
            "influence over what becomes canonical."
        ),
        node_type="concept",
        status="developing",
        tags=["business-model", "reviewers", "incentives", "economics"],
    )
    store.add_node(reviewer_economics)

    continuity_standard = Node(
        title="Continuity Standard as Moat",
        description=(
            "The Continuity Standard (v0.1 published) defines how "
            "knowledge should be structured, versioned, and governed "
            "on NodeRail. If other platforms adopt this standard, "
            "NodeRail becomes the reference implementation — similar "
            "to how HTTP is a standard and Apache/Nginx are "
            "implementations. Standards are the strongest possible moat "
            "because they create ecosystem lock-in without vendor "
            "lock-in."
        ),
        node_type="concept",
        status="developing",
        tags=["strategy", "standard", "moat", "continuity"],
    )
    store.add_node(continuity_standard)

    # ===================================================================
    # INQUIRIES
    # ===================================================================

    inquiry_pricing = Node(
        title="What should institutional pricing look like?",
        description=(
            "Open question: What pricing model works for institutions? "
            "Per-seat? Per-DOI? Flat annual license? Tiered by size? "
            "Need to research what universities and labs actually pay "
            "for comparable infrastructure (journal subscriptions, "
            "research tools, data platforms)."
        ),
        node_type="inquiry",
        status="exploratory",
        tags=["business-model", "pricing", "institutions"],
    )
    store.add_node(inquiry_pricing)

    inquiry_ai_pricing = Node(
        title="How should AI API access be priced?",
        description=(
            "Open question: Per-query? Per-node accessed? Flat monthly? "
            "Based on training data volume consumed? Need to balance "
            "accessibility with fair compensation for authors whose "
            "work is being consumed."
        ),
        node_type="inquiry",
        status="exploratory",
        tags=["business-model", "pricing", "AI", "API"],
    )
    store.add_node(inquiry_ai_pricing)

    inquiry_trust = Node(
        title="How do we earn institutional trust fast?",
        description=(
            "Critical question: Institutions move slowly. What accelerates "
            "trust? Options: (1) publish HCS as a complete case study; "
            "(2) partner with one credible institution early; (3) get "
            "the Continuity Standard cited in an academic paper; "
            "(4) demonstrate DOI-backed governance that journals can't "
            "match; (5) approach through compliance angle, not feature "
            "angle."
        ),
        node_type="inquiry",
        status="developing",
        tags=["strategy", "trust", "go-to-market"],
    )
    store.add_node(inquiry_trust)

    # ===================================================================
    # RELATIONSHIPS
    # ===================================================================

    relationships = [
        # Business model → NodeRail
        (biz_model, noderail_node, "applies_to",
         "Revenue model for the NodeRail platform"),

        # Layers → business model
        (layer_free, biz_model, "supports",
         "Growth engine that builds graph density"),
        (layer_institutional, biz_model, "supports",
         "Primary near-term revenue source"),
        (layer_ai_api, biz_model, "supports",
         "Strategic long-term revenue source"),
        (layer_doi, biz_model, "supports",
         "Transaction layer for citation services"),

        # Strategic concepts → business model
        (flywheel, biz_model, "supports",
         "Self-reinforcing growth loop"),
        (compliance_positioning, layer_ai_api, "supports",
         "Makes AI API a compliance play, not just a feature"),
        (reviewer_economics, layer_institutional, "supports",
         "How reviewers get compensated through institutional revenue"),
        (continuity_standard, biz_model, "supports",
         "Standards create the strongest moat"),

        # Flywheel connections
        (layer_free, flywheel, "supports",
         "Free publishing drives graph density"),
        (layer_ai_api, flywheel, "supports",
         "AI revenue funds reviews which drive more publishing"),
        (layer_institutional, flywheel, "supports",
         "Institutions bring researchers who publish and review"),

        # Inquiries
        (inquiry_pricing, layer_institutional, "extends",
         "Pricing model for institutional layer"),
        (inquiry_ai_pricing, layer_ai_api, "extends",
         "Pricing model for AI API layer"),
        (inquiry_trust, biz_model, "extends",
         "Go-to-market trust question"),
    ]

    for source, target, rel_type, desc in relationships:
        edge = Edge(
            source_id=source.id,
            target_id=target.id,
            relationship=rel_type,
            description=desc,
        )
        store.add_edge(edge)

    print("=" * 50)
    print("BUSINESS MODEL SEEDED")
    print("=" * 50)
    print(f"  New structures:    11")
    print(f"  New connections:   {len(relationships)}")
    print(f"  Total nodes now:   {store.stats()['total_nodes']}")
    print(f"  Total edges now:   {store.stats()['total_edges']}")
    print()


if __name__ == "__main__":
    seed()
