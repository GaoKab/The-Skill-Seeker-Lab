"""
NodeRail Seed Script — Human Capacity Science (HCS) Ecosystem

Seeds the NodeRail graph with real intellectual structures from
the HCS body of work: frameworks, concepts, measurements, inquiries,
projects, and field notes — with relationships and evolution history.

Run: python seed_hcs.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from noderail.models import Node, Edge, Version, Institution, Member, Review, _now
from noderail.storage import NodeRailStore


def seed():
    store = NodeRailStore()

    # Check if already seeded
    if store.stats()["total_nodes"] > 0:
        print("Graph already has data. To re-seed, delete noderail_data.json first.")
        return

    # ===================================================================
    # FRAMEWORKS
    # ===================================================================

    hcs = Node(
        title="Human Capacity Science",
        description=(
            "A structured framework for understanding, measuring, and "
            "optimizing the total usable capacity of a human being at any "
            "given time. HCS treats capacity not as a fixed trait but as a "
            "dynamic, fluctuating resource shaped by cognitive load, emotional "
            "residue, environmental strain, and recovery patterns. It provides "
            "the theoretical foundation for instruments like HBI and applied "
            "systems like DustOff."
        ),
        node_type="framework",
        status="developing",
        tags=["capacity", "human-systems", "core-framework"],
    )

    capacity_window = Node(
        title="Capacity Window Model",
        description=(
            "A model describing the dynamic window of usable capacity "
            "available to a person at any point in time. The window expands "
            "and contracts based on load, recovery, emotional state, and "
            "environmental conditions. Defines states: open (high available "
            "capacity), narrowing (capacity under pressure), constricted "
            "(minimal usable capacity), and recovering (capacity rebuilding)."
        ),
        node_type="framework",
        status="developing",
        tags=["capacity", "states", "model"],
    )

    adoption_systems = Node(
        title="Adoption Systems Design",
        description=(
            "A framework for understanding how new tools, processes, and "
            "systems get adopted — or fail to get adopted — by humans. "
            "Integrates capacity constraints with adoption friction, arguing "
            "that adoption failure is often a capacity problem, not a "
            "willingness problem."
        ),
        node_type="framework",
        status="exploratory",
        tags=["adoption", "systems", "capacity"],
    )

    # ===================================================================
    # CONCEPTS
    # ===================================================================

    human_capacity = Node(
        title="Human Capacity",
        description=(
            "The total usable cognitive, emotional, and physical resource "
            "available to a person at a given time. Not a fixed trait — "
            "a dynamic, context-dependent state that fluctuates based on "
            "load, strain, recovery, and environment. The foundational "
            "construct of HCS."
        ),
        node_type="concept",
        status="stable",
        tags=["capacity", "core-construct"],
    )

    emotional_residue = Node(
        title="Emotional Residue",
        description=(
            "The lingering cognitive and emotional load that persists after "
            "a difficult interaction, decision, or experience — even after "
            "the situation has ended. Emotional residue occupies capacity "
            "without the person's conscious awareness, creating a hidden "
            "drain on available bandwidth."
        ),
        node_type="concept",
        status="developing",
        tags=["capacity", "emotion", "hidden-load"],
    )

    capacity_leakage = Node(
        title="Capacity Leakage",
        description=(
            "The gradual, often invisible loss of usable capacity through "
            "micro-stressors, unresolved tasks, ambient noise, and "
            "environmental friction. Unlike acute load (which is felt), "
            "leakage is cumulative and typically unnoticed until the "
            "person is already in a constricted state."
        ),
        node_type="concept",
        status="developing",
        tags=["capacity", "drain", "invisible-load"],
    )

    digital_fatigue = Node(
        title="Digital Fatigue",
        description=(
            "A specific form of capacity drain caused by sustained "
            "interaction with digital systems — screens, notifications, "
            "context-switching between apps, information overload. "
            "Distinct from general tiredness; it specifically degrades "
            "the capacity for focused cognitive work."
        ),
        node_type="concept",
        status="exploratory",
        tags=["capacity", "digital", "fatigue"],
    )

    rogue_work = Node(
        title="Rogue Work",
        description=(
            "Work that falls outside any defined process, role, or system — "
            "the untracked labor that people perform to fill gaps, fix "
            "breakdowns, or compensate for system failures. Rogue work "
            "consumes significant capacity but is invisible to management "
            "systems and productivity metrics."
        ),
        node_type="concept",
        status="developing",
        tags=["capacity", "work", "invisible-labor"],
    )

    adoption_friction = Node(
        title="Adoption Friction",
        description=(
            "The resistance a person experiences when asked to adopt a "
            "new tool, process, or behavior. Not simply resistance to "
            "change — it is the gap between the capacity required to "
            "adopt and the capacity currently available. High adoption "
            "friction occurs when systems demand more than the user "
            "can give."
        ),
        node_type="concept",
        status="developing",
        tags=["adoption", "capacity", "friction"],
    )

    emotional_carryover = Node(
        title="Emotional Carryover",
        description=(
            "The transfer of emotional load from one context to another — "
            "bringing the weight of a difficult morning into an afternoon "
            "meeting, or carrying work strain into personal relationships. "
            "An extension of emotional residue that tracks how emotional "
            "load moves across domains."
        ),
        node_type="concept",
        status="exploratory",
        tags=["capacity", "emotion", "transfer"],
    )

    # ===================================================================
    # MEASUREMENTS
    # ===================================================================

    hbi = Node(
        title="Human Bandwidth Index (HBI)",
        description=(
            "A composite measurement instrument for assessing a person's "
            "current usable capacity across cognitive, emotional, and "
            "environmental dimensions. Designed to be lightweight enough "
            "for repeated use (not a one-time diagnostic) while capturing "
            "enough signal to identify capacity states and predict "
            "narrowing windows."
        ),
        node_type="measurement",
        status="developing",
        tags=["capacity", "measurement", "instrument"],
    )

    capacity_states = Node(
        title="Capacity Window States",
        description=(
            "The classification system for identifying where a person "
            "sits within the Capacity Window Model: open, narrowing, "
            "constricted, or recovering. Each state has observable "
            "indicators and different implications for what kinds of "
            "work, decisions, or interactions are feasible."
        ),
        node_type="measurement",
        status="developing",
        tags=["capacity", "states", "classification"],
    )

    signal_clusters = Node(
        title="Signal Clusters",
        description=(
            "Groupings of behavioral, contextual, and self-reported "
            "signals that, taken together, indicate a particular capacity "
            "state. No single signal is diagnostic — clusters provide "
            "the pattern recognition layer for HBI and capacity "
            "assessment."
        ),
        node_type="measurement",
        status="exploratory",
        tags=["capacity", "signals", "patterns"],
    )

    # ===================================================================
    # INQUIRIES
    # ===================================================================

    inquiry_strain = Node(
        title="How does interpersonal strain distort usable capacity?",
        description=(
            "An active research question exploring how conflict, tension, "
            "and difficult relationships consume capacity in ways that "
            "are disproportionate to the actual cognitive demands involved. "
            "Interpersonal strain may be the single largest hidden drain "
            "on human bandwidth."
        ),
        node_type="inquiry",
        status="developing",
        tags=["capacity", "interpersonal", "strain"],
    )

    inquiry_digital_vs_emotional = Node(
        title="What differentiates digital fatigue from emotional residue?",
        description=(
            "Are digital fatigue and emotional residue distinct phenomena, "
            "or is digital fatigue a subtype of emotional residue operating "
            "through a technological medium? If distinct, what are the "
            "differential indicators and recovery patterns?"
        ),
        node_type="inquiry",
        status="exploratory",
        tags=["capacity", "digital", "emotion", "differential"],
    )

    inquiry_signals = Node(
        title="What signals best predict narrowing capacity windows?",
        description=(
            "Investigating which observable signals — behavioral changes, "
            "environmental conditions, self-report patterns — most "
            "reliably predict that a person's capacity window is about "
            "to narrow. Early detection would enable preemptive "
            "intervention rather than reactive recovery."
        ),
        node_type="inquiry",
        status="developing",
        tags=["capacity", "prediction", "signals"],
    )

    inquiry_rogue = Node(
        title="What is the capacity cost of rogue work?",
        description=(
            "Attempting to quantify how much capacity is consumed by "
            "work that exists outside formal systems. If rogue work is "
            "invisible to management but real to the person doing it, "
            "what fraction of total capacity does it absorb? And what "
            "happens when that fraction is acknowledged?"
        ),
        node_type="inquiry",
        status="exploratory",
        tags=["capacity", "rogue-work", "quantification"],
    )

    # ===================================================================
    # PROJECTS
    # ===================================================================

    dustoff = Node(
        title="DustOff Reset",
        description=(
            "An applied project that operationalizes Human Capacity Science "
            "into a practical reset system. DustOff helps individuals "
            "recognize when they are in a constricted capacity state and "
            "provides structured pathways back to an open window — not "
            "through productivity hacks but through capacity-aware recovery."
        ),
        node_type="project",
        status="developing",
        tags=["capacity", "application", "recovery", "product"],
    )

    noderail = Node(
        title="NodeRail",
        description=(
            "A publishing system for living knowledge — the infrastructure "
            "layer for building, connecting, and evolving bodies of thought "
            "with provenance, version history, and structural relationships. "
            "Born from the need to give HCS and related intellectual work "
            "a home that preserves lineage and attribution."
        ),
        node_type="project",
        status="developing",
        tags=["infrastructure", "knowledge", "publishing", "product"],
    )

    wci = Node(
        title="Workflow Capacity Intelligence",
        description=(
            "An organizational application of HCS that brings capacity "
            "awareness into workplace systems. WCI translates individual "
            "capacity signals into team-level and organizational-level "
            "intelligence — identifying where capacity is being wasted, "
            "where systems are creating hidden load, and where "
            "interventions would have the highest impact."
        ),
        node_type="project",
        status="exploratory",
        tags=["capacity", "organizational", "workplace", "product"],
    )

    # ===================================================================
    # FIELD NOTES
    # ===================================================================

    fn_rogue_mismatch = Node(
        title="Rogue work and available capacity mismatch",
        description=(
            "Observation: People who report feeling 'busy but unproductive' "
            "are often doing significant rogue work — labor that doesn't "
            "show up in any system but is essential to keeping things "
            "running. The mismatch between perceived productivity and "
            "actual capacity expenditure suggests that our measurement "
            "of 'productivity' is fundamentally broken."
        ),
        node_type="field_note",
        status="developing",
        tags=["rogue-work", "productivity", "observation"],
    )

    fn_overload_episodes = Node(
        title="Overload episodes follow predictable patterns",
        description=(
            "Observation: Capacity collapse rarely happens suddenly. "
            "There is almost always a 2-3 day narrowing period where "
            "signals are visible in retrospect — shorter responses, "
            "avoidance of complex tasks, increased irritability, "
            "preference for low-demand activities. This suggests "
            "early detection is feasible."
        ),
        node_type="field_note",
        status="developing",
        tags=["capacity", "patterns", "prediction", "observation"],
    )

    fn_recovery_nonlinear = Node(
        title="Recovery from constriction is nonlinear",
        description=(
            "Observation: Moving from a constricted capacity state back "
            "to an open one does not follow a smooth curve. There are "
            "false recoveries — periods where capacity appears restored "
            "but collapses again under minor load. True recovery seems "
            "to require a sustained low-demand period, not just a "
            "single rest event."
        ),
        node_type="field_note",
        status="exploratory",
        tags=["capacity", "recovery", "nonlinear", "observation"],
    )

    # ===================================================================
    # ADD ALL NODES
    # ===================================================================

    all_nodes = [
        hcs, capacity_window, adoption_systems,
        human_capacity, emotional_residue, capacity_leakage,
        digital_fatigue, rogue_work, adoption_friction,
        emotional_carryover,
        hbi, capacity_states, signal_clusters,
        inquiry_strain, inquiry_digital_vs_emotional,
        inquiry_signals, inquiry_rogue,
        dustoff, noderail, wci,
        fn_rogue_mismatch, fn_overload_episodes, fn_recovery_nonlinear,
    ]

    for node in all_nodes:
        store.add_node(node)
        print(f"  + {node.node_type:12s}  {node.title}")

    print(f"\nEstablished {len(all_nodes)} structures.\n")

    # ===================================================================
    # RELATIONSHIPS
    # ===================================================================

    relationships = [
        # Core framework structure
        (human_capacity, hcs, "supports",
         "Foundational construct that HCS is built around"),
        (capacity_window, hcs, "extends",
         "Extends HCS into a dynamic state model"),
        (adoption_systems, hcs, "extends",
         "Applies capacity thinking to adoption and change"),

        # Concepts → HCS
        (emotional_residue, hcs, "supports",
         "Identifies a key mechanism of hidden capacity drain"),
        (capacity_leakage, hcs, "supports",
         "Describes the gradual, invisible loss pattern"),
        (digital_fatigue, hcs, "supports",
         "Specific domain application of capacity drain"),
        (rogue_work, hcs, "supports",
         "Reveals invisible labor as a capacity factor"),
        (adoption_friction, adoption_systems, "supports",
         "Core construct within Adoption Systems Design"),

        # Concept-to-concept relationships
        (emotional_carryover, emotional_residue, "extends",
         "Extends residue concept to cross-domain transfer"),
        (digital_fatigue, emotional_residue, "challenges",
         "May be a subtype rather than a separate phenomenon"),
        (adoption_friction, human_capacity, "applies_to",
         "Adoption friction is capacity applied to change contexts"),
        (capacity_leakage, rogue_work, "supports",
         "Rogue work is a major source of capacity leakage"),

        # Measurements → frameworks and concepts
        (hbi, hcs, "derives_from",
         "Primary measurement instrument derived from HCS theory"),
        (hbi, human_capacity, "operationalizes",
         "Makes the abstract concept of capacity measurable"),
        (capacity_states, capacity_window, "derives_from",
         "Classification system derived from the window model"),
        (signal_clusters, hbi, "supports",
         "Pattern recognition layer that feeds into HBI"),
        (signal_clusters, capacity_states, "applies_to",
         "Clusters map to specific capacity states"),

        # Inquiries → concepts and frameworks
        (inquiry_strain, hcs, "extends",
         "Exploring interpersonal strain as a capacity factor"),
        (inquiry_strain, emotional_residue, "extends",
         "Strain as a potent source of emotional residue"),
        (inquiry_digital_vs_emotional, digital_fatigue, "challenges",
         "Questioning whether digital fatigue is truly distinct"),
        (inquiry_digital_vs_emotional, emotional_residue, "challenges",
         "Questioning the boundary between these phenomena"),
        (inquiry_signals, capacity_states, "extends",
         "Seeking predictive signals for state transitions"),
        (inquiry_signals, signal_clusters, "extends",
         "Building on cluster work toward prediction"),
        (inquiry_rogue, rogue_work, "extends",
         "Attempting to quantify what was previously invisible"),

        # Projects → frameworks
        (dustoff, hcs, "operationalizes",
         "Turns HCS theory into a practical recovery system"),
        (dustoff, capacity_window, "operationalizes",
         "Uses window states to guide recovery pathways"),
        (noderail, hcs, "supports",
         "Infrastructure born from the need to house HCS properly"),
        (wci, hcs, "operationalizes",
         "Brings capacity intelligence to organizational level"),
        (wci, signal_clusters, "operationalizes",
         "Uses signal clusters for team-level capacity awareness"),

        # Field notes → concepts and inquiries
        (fn_rogue_mismatch, rogue_work, "supports",
         "Direct observation supporting the rogue work concept"),
        (fn_rogue_mismatch, inquiry_rogue, "supports",
         "Grounded evidence feeding the rogue work inquiry"),
        (fn_overload_episodes, capacity_states, "supports",
         "Suggests state transitions have observable precursors"),
        (fn_overload_episodes, inquiry_signals, "supports",
         "Evidence that early detection signals exist"),
        (fn_recovery_nonlinear, capacity_window, "refines",
         "Refines understanding of recovery within the window model"),
        (fn_recovery_nonlinear, dustoff, "supports",
         "Informs DustOff's approach to recovery design"),
    ]

    for source, target, rel_type, desc in relationships:
        edge = Edge(
            source_id=source.id,
            target_id=target.id,
            relationship=rel_type,
            description=desc,
        )
        store.add_edge(edge)

    print(f"Connected {len(relationships)} relationships.\n")

    # ===================================================================
    # EVOLUTION HISTORY (for key structures)
    # ===================================================================

    # HCS evolution
    hcs_v2 = Version(
        node_id=hcs.id,
        version_number=2,
        evolution_type="extension",
        title="Human Capacity Science",
        description=hcs.description,
        changes=(
            "Expanded from individual capacity model to include "
            "environmental and interpersonal dimensions. Capacity is "
            "not just internal — it is shaped by context."
        ),
    )
    store.add_version(hcs_v2)

    hcs_v3 = Version(
        node_id=hcs.id,
        version_number=3,
        evolution_type="refinement",
        title="Human Capacity Science",
        description=hcs.description,
        changes=(
            "Tightened the distinction between capacity (dynamic state) "
            "and capability (stable trait). HCS measures the former, not "
            "the latter. This resolves confusion with competency frameworks."
        ),
    )
    store.add_version(hcs_v3)

    # HBI evolution
    hbi_v2 = Version(
        node_id=hbi.id,
        version_number=2,
        evolution_type="refinement",
        title="Human Bandwidth Index (HBI)",
        description=hbi.description,
        changes=(
            "Shifted from a single composite score to a multi-dimensional "
            "profile. A single number obscured important distinctions "
            "between cognitive and emotional capacity states."
        ),
    )
    store.add_version(hbi_v2)

    # Emotional residue evolution
    er_v2 = Version(
        node_id=emotional_residue.id,
        version_number=2,
        evolution_type="extension",
        title="Emotional Residue",
        description=emotional_residue.description,
        changes=(
            "Added temporal dimension — residue does not just exist, "
            "it decays at different rates depending on the source. "
            "Interpersonal residue decays slowest."
        ),
    )
    store.add_version(er_v2)

    # Capacity Window evolution
    cw_v2 = Version(
        node_id=capacity_window.id,
        version_number=2,
        evolution_type="reinterpretation",
        title="Capacity Window Model",
        description=capacity_window.description,
        changes=(
            "Reframed from a binary open/closed model to a spectrum "
            "with four states (open, narrowing, constricted, recovering). "
            "This better captures the transitional nature of capacity."
        ),
    )
    store.add_version(cw_v2)

    # DustOff evolution
    dustoff_v2 = Version(
        node_id=dustoff.id,
        version_number=2,
        evolution_type="application",
        title="DustOff Reset",
        description=dustoff.description,
        changes=(
            "Moved from conceptual design to structured reset protocol. "
            "First version of the capacity-aware recovery pathway "
            "based on window states."
        ),
    )
    store.add_version(dustoff_v2)

    print("Added evolution history to 5 structures.\n")

    # ===================================================================
    # INSTITUTIONS
    # ===================================================================

    hcs_lab = Institution(
        name="Human Capacity Science Lab",
        institution_type="research_lab",
        description=(
            "The founding research lab for Human Capacity Science. "
            "Develops the core frameworks, measurements, and applied "
            "systems that make up the HCS body of work."
        ),
        website="https://noderail.web.app",
    )
    store.add_institution(hcs_lab)

    sfi = Institution(
        name="Santa Fe Institute",
        institution_type="research_lab",
        description=(
            "Independent research institute focused on complex adaptive "
            "systems. Potential collaborator on capacity modeling and "
            "systems-level human performance research."
        ),
        website="https://santafe.edu",
    )
    store.add_institution(sfi)

    mit_media = Institution(
        name="MIT Media Lab",
        institution_type="university",
        description=(
            "Interdisciplinary research lab at MIT. Relevant work on "
            "human-computer interaction, digital wellbeing, and "
            "cognitive load in technological environments."
        ),
        website="https://media.mit.edu",
    )
    store.add_institution(mit_media)

    print(f"  + 3 institutions registered\n")

    # ===================================================================
    # MEMBERS
    # ===================================================================

    # HCS Lab members
    founder = Member(
        name="Gao Kab",
        institution_id=hcs_lab.id,
        role="admin",
        expertise="Human Capacity Science, framework design, systems thinking",
    )
    store.add_member(founder)

    hcs_researcher_1 = Member(
        name="Dr. Amara Chen",
        institution_id=hcs_lab.id,
        role="researcher",
        expertise="Cognitive load measurement, psychometrics",
    )
    store.add_member(hcs_researcher_1)

    # SFI reviewers
    sfi_reviewer_1 = Member(
        name="Dr. Marcus Torres",
        institution_id=sfi.id,
        role="reviewer",
        expertise="Complex systems, dynamical modeling, human performance",
    )
    store.add_member(sfi_reviewer_1)

    sfi_reviewer_2 = Member(
        name="Dr. Leah Okonkwo",
        institution_id=sfi.id,
        role="reviewer",
        expertise="Network science, organizational behavior, resilience theory",
    )
    store.add_member(sfi_reviewer_2)

    # MIT reviewers
    mit_reviewer_1 = Member(
        name="Dr. Raj Patel",
        institution_id=mit_media.id,
        role="reviewer",
        expertise="Digital wellbeing, HCI, attention economics",
    )
    store.add_member(mit_reviewer_1)

    mit_researcher_1 = Member(
        name="Dr. Sofia Andersson",
        institution_id=mit_media.id,
        role="researcher",
        expertise="Emotional computing, physiological measurement, UX research",
    )
    store.add_member(mit_researcher_1)

    print(f"  + 6 members added across 3 institutions\n")

    # ===================================================================
    # SAMPLE REVIEWS
    # ===================================================================

    # Review 1: HCS framework reviewed by SFI complex systems expert
    review_hcs = Review(
        node_id=hcs.id,
        reviewer_id=sfi_reviewer_1.id,
        verdict="validated",
        status="completed",
        completed_at=_now(),
        is_rigorous=(
            "The framework demonstrates strong internal coherence. "
            "The distinction between capacity (dynamic state) and "
            "capability (stable trait) is well-drawn and addresses a "
            "genuine gap in existing human performance models. The "
            "multi-dimensional approach to capacity is sound."
        ),
        is_novel=(
            "Yes. While individual components (cognitive load, emotional "
            "regulation, environmental factors) exist in separate "
            "literatures, the integration into a unified dynamic capacity "
            "model is genuinely new. The treatment of capacity as a "
            "fluctuating resource rather than a fixed attribute is the "
            "key innovation."
        ),
        what_is_missing=(
            "The framework would benefit from more formal mathematical "
            "specification of capacity dynamics — how the window opens "
            "and closes, what the interaction terms are between "
            "dimensions. Currently the model is qualitative."
        ),
        summary=(
            "Human Capacity Science represents a legitimate new framework "
            "with clear differentiation from existing models. Validated "
            "as a developing framework with strong foundations. "
            "Recommend advancing to stable status once the measurement "
            "instruments (HBI) are formally specified."
        ),
        requested_by=founder.id,
    )
    store.add_review(review_hcs)

    # Review 2: HBI reviewed by MIT measurement expert
    review_hbi = Review(
        node_id=hbi.id,
        reviewer_id=mit_reviewer_1.id,
        verdict="needs_revision",
        status="completed",
        completed_at=_now(),
        is_rigorous=(
            "The conceptual basis for HBI is solid — measuring "
            "bandwidth across cognitive, emotional, and environmental "
            "dimensions is well-motivated. However, the instrument "
            "specification needs more detail on item construction, "
            "scoring methodology, and psychometric validation plans."
        ),
        is_novel=(
            "The multi-dimensional, repeatable-use design is "
            "differentiated from existing instruments (which tend to "
            "be one-time assessments). The idea of lightweight "
            "repeated measurement of capacity state is new and "
            "practically valuable."
        ),
        what_is_missing=(
            "1. Formal item pool and scoring rubric. "
            "2. Pilot validation data. "
            "3. Test-retest reliability plan. "
            "4. Sensitivity analysis — can HBI detect the state "
            "changes the Capacity Window Model predicts?"
        ),
        summary=(
            "HBI has a strong theoretical foundation and a genuine "
            "gap to fill. It is not yet at measurement-ready status. "
            "Needs a formal specification round before it can be "
            "validated as an instrument."
        ),
        requested_by=founder.id,
    )
    store.add_review(review_hbi)

    # Review 3: Emotional Residue reviewed as novel concept
    review_er = Review(
        node_id=emotional_residue.id,
        reviewer_id=sfi_reviewer_2.id,
        verdict="novel",
        status="completed",
        completed_at=_now(),
        is_rigorous=(
            "The concept is clearly defined and distinguishable from "
            "adjacent constructs (stress, burnout, emotional labor). "
            "The temporal dimension — residue decaying at different "
            "rates depending on source — adds meaningful specificity."
        ),
        is_novel=(
            "Yes. While emotional aftereffects are discussed in "
            "psychology, the framing of 'residue' as an invisible "
            "capacity drain with differential decay rates is a "
            "genuinely new conceptual contribution. The connection "
            "to capacity (rather than to mood or wellbeing) is the "
            "distinguishing move."
        ),
        what_is_missing=(
            "Empirical grounding. The concept is well-articulated "
            "theoretically but needs observational data. What does "
            "emotional residue look like in measurable terms? How "
            "would you detect it in real time?"
        ),
        summary=(
            "Emotional Residue is a novel concept that fills a real "
            "gap between emotional experience and capacity theory. "
            "Recommend advancing and connecting to measurement work."
        ),
        requested_by=founder.id,
    )
    store.add_review(review_er)

    # One pending review
    review_pending = Review(
        node_id=capacity_window.id,
        reviewer_id=sfi_reviewer_1.id,
        verdict="",
        status="requested",
        requested_by=founder.id,
    )
    store.add_review(review_pending)

    print(f"  + 3 completed reviews, 1 pending\n")

    # ===================================================================
    # SUMMARY
    # ===================================================================

    stats = store.stats()
    institutions = store.get_all_institutions()
    members = store.get_all_members()
    completed_reviews = store.get_completed_reviews()
    pending_reviews = store.get_pending_reviews()

    print("=" * 50)
    print("SEED COMPLETE")
    print("=" * 50)
    print(f"  Nodes:        {stats['total_nodes']}")
    print(f"  Connections:  {stats['total_edges']}")
    print(f"  Versions:     {stats['total_versions']}")
    print(f"  Institutions: {len(institutions)}")
    print(f"  Members:      {len(members)}")
    print(f"  Reviews:      {len(completed_reviews)} completed, {len(pending_reviews)} pending")
    print()
    print("  By type:")
    for t, count in stats["by_type"].items():
        if count > 0:
            print(f"    {t:15s} {count}")
    print()
    print("  By status:")
    for s, count in stats["by_status"].items():
        if count > 0:
            print(f"    {s:15s} {count}")
    print()
    print("Run: streamlit run noderail_app.py")


if __name__ == "__main__":
    seed()
