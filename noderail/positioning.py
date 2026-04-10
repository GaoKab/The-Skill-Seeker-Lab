"""
NodeRail Competitor Positioning & Messaging

Strategic reference document. Not executable code.
Defines how NodeRail differentiates from adjacent tools and platforms,
with ready-to-use language for conversations, pitch decks, and copy.
"""


# ===================================================================
# CATEGORY DEFINITION
# ===================================================================

CATEGORY = {
    "name": "Structured Research Publishing",
    "definition": (
        "A new category at the intersection of knowledge management, "
        "academic publishing, and research infrastructure. Structured "
        "Research Publishing treats ideas as evolving, interconnected "
        "objects with typed relationships, expert review, version "
        "lineage, and persistent identifiers — not as static documents "
        "trapped in filing cabinets or wikis."
    ),
    "why_new_category": (
        "Existing tools force a false choice: flexible-but-unstructured "
        "(Notion, Obsidian) or rigorous-but-rigid (journals, Zenodo). "
        "NodeRail occupies the space between, where serious intellectual "
        "work needs both structure and fluidity."
    ),
}


# ===================================================================
# TAGLINE OPTIONS
# ===================================================================

TAGLINES = [
    "A publishing system for living knowledge.",
    "Where ideas evolve, connect, and earn their DOI.",
    "Structure your thinking. Publish your lineage.",
    "From working idea to citable artifact — with lineage intact.",
    "The research environment where knowledge grows up in public.",
    "Build bodies of thought, not piles of documents.",
    "Your intellectual work deserves infrastructure.",
]


# ===================================================================
# ELEVATOR PITCHES
# ===================================================================

ELEVATOR_PITCH_30_SEC = (
    "NodeRail is a publishing system for living knowledge. Researchers "
    "create structured objects — concepts, frameworks, measurements — "
    "and connect them with typed relationships like 'extends,' "
    "'challenges,' or 'operationalizes.' Every change is versioned. "
    "Expert reviewers validate the work. And when it's ready, NodeRail "
    "issues a DOI — a permanent, citable identifier — with the full "
    "lineage baked in. It's how research should have always worked: "
    "ideas that grow, connect, and earn credibility in the open."
)

ELEVATOR_PITCH_2_MIN = (
    "Right now, the lifecycle of a research idea is broken. You think "
    "in a private tool like Notion or Obsidian, then you write it up "
    "as a static paper, submit it to a journal that takes months to "
    "review, and if it gets published, it sits as a PDF that nobody "
    "can build on programmatically.\n\n"

    "NodeRail fixes this by treating intellectual work as a living "
    "graph, not a stack of documents. You create typed structures — "
    "a concept, a framework, a measurement instrument — and connect "
    "them with relationships that have real meaning: 'derives from,' "
    "'extends,' 'challenges.' Every change is tracked as an evolution "
    "with its own type: refinement, extension, divergence, split. "
    "You're building lineage, not just version history.\n\n"

    "When the work is mature, you request expert review through the "
    "platform. Reviewers evaluate rigor and novelty using a structured "
    "rubric. If validated, the structure advances to stable status and "
    "receives a DOI — a permanent identifier issued through Zenodo — "
    "with the review, the lineage, and the connections all embedded "
    "in the metadata.\n\n"

    "For institutions, NodeRail provides a shared environment where "
    "labs, departments, or entire universities can see how their "
    "intellectual output connects and evolves. For AI developers, "
    "we offer an API to structured, expert-reviewed knowledge — not "
    "scraped web pages, but validated research objects with provenance.\n\n"

    "We're not a note-taking app. We're not a journal. We're the "
    "infrastructure layer for how knowledge gets built, validated, "
    "and made permanent."
)


# ===================================================================
# COMPETITOR POSITIONING
# ===================================================================
# Each entry contains:
#   differentiator — sharp one-liner ("X but not Y" format)
#   does_well      — honest acknowledgment of competitor strength
#   lacks          — what they lack that NodeRail provides
#   when_asked     — response script for conversations

COMPETITORS = {

    "notion": {
        "differentiator": (
            "Notion organizes your work. NodeRail publishes it — with "
            "DOIs, expert review, and permanent lineage."
        ),
        "does_well": (
            "Flexible workspace for teams. Excellent for internal docs, "
            "project management, and lightweight databases. Low friction "
            "for getting started."
        ),
        "lacks": (
            "No concept of intellectual rigor. No typed relationships "
            "between ideas. No version lineage. No expert review. No "
            "DOIs. No way to make work citable or permanent. Everything "
            "lives inside a proprietary silo with no scholarly identity."
        ),
        "when_asked": (
            "If someone says 'How is this different from Notion?' — "
            "say: 'Notion is a workspace. NodeRail is a publishing "
            "system. In Notion, you organize pages. In NodeRail, you "
            "build typed intellectual structures — concepts, frameworks, "
            "measurements — with explicit relationships and evolution "
            "tracking. When your work is reviewed by an expert, it gets "
            "a DOI. Notion will never give your ideas a permanent "
            "citable identity.'"
        ),
    },

    "obsidian": {
        "differentiator": (
            "Obsidian links your notes. NodeRail structures your "
            "knowledge and makes it citable."
        ),
        "does_well": (
            "Excellent local-first markdown editor. Bidirectional "
            "linking, graph view, plugin ecosystem. Beloved by personal "
            "knowledge management enthusiasts. Owns your files."
        ),
        "lacks": (
            "Links are untyped — a link is a link is a link. No "
            "distinction between 'extends' and 'challenges.' No version "
            "lineage (just file history). No expert review. No DOIs. "
            "No institutional layer. No collaboration model for "
            "research teams. The graph looks impressive but carries "
            "no semantic weight."
        ),
        "when_asked": (
            "If someone says 'How is this different from Obsidian?' — "
            "say: 'Obsidian is a personal knowledge base with links. "
            "NodeRail is a shared research environment with typed "
            "relationships. In Obsidian, linking two notes tells you "
            "nothing about *how* they relate. In NodeRail, every "
            "connection has meaning — derives from, challenges, "
            "operationalizes. Plus, your work can be reviewed, "
            "validated, and issued a DOI. Obsidian is for thinking. "
            "NodeRail is for publishing what you've thought.'"
        ),
    },

    "roam_research": {
        "differentiator": (
            "Roam captures the process of thinking. NodeRail captures "
            "the structure of knowledge — and makes it permanent."
        ),
        "does_well": (
            "Pioneered networked thought, block-level references, and "
            "daily-note workflows. Strong for brainstorming and "
            "associative exploration."
        ),
        "lacks": (
            "Designed for personal ideation, not for publishing or "
            "validation. No typed relationships. No status progression "
            "(exploratory to canonical). No expert review. No DOIs. "
            "No institutional support. Knowledge stays informal and "
            "private."
        ),
        "when_asked": (
            "If someone says 'How is this different from Roam?' — "
            "say: 'Roam is designed for the messy early phase of "
            "thinking — and it's great at that. NodeRail picks up "
            "where Roam stops. When your thinking has enough shape "
            "to be a concept or a framework, NodeRail gives it "
            "structure, tracks its evolution, connects it to a "
            "larger body of work, and lets an expert review it for "
            "a DOI. Roam is upstream; NodeRail is downstream.'"
        ),
    },

    "researchgate": {
        "differentiator": (
            "ResearchGate shares finished papers. NodeRail publishes "
            "the living structures underneath them."
        ),
        "does_well": (
            "Large academic social network. Good for sharing published "
            "papers, finding collaborators, and tracking citations. "
            "Familiar to academics."
        ),
        "lacks": (
            "Still paper-centric — you upload a PDF and wait for "
            "citations. No structured knowledge objects. No typed "
            "relationships between ideas across papers. No version "
            "lineage within a single evolving concept. No expert review "
            "on the platform itself. No DOI issuance. Essentially a "
            "social network bolted onto a document repository."
        ),
        "when_asked": (
            "If someone says 'How is this different from ResearchGate?' "
            "— say: 'ResearchGate is a social network for sharing "
            "finished papers. NodeRail is a publishing system for the "
            "ideas inside those papers. On ResearchGate, a concept "
            "spread across five papers has no unified identity. On "
            "NodeRail, that concept is a single structure with its own "
            "lineage, connections, reviews, and DOI. We make the "
            "intellectual work itself the unit — not the document.'"
        ),
    },

    "github": {
        "differentiator": (
            "GitHub versions code. NodeRail versions knowledge — with "
            "evolution types, expert review, and DOIs."
        ),
        "does_well": (
            "Industry-standard version control. Pull requests, code "
            "review, issue tracking, CI/CD. Collaboration model that "
            "software engineers trust."
        ),
        "lacks": (
            "Designed for code, not for intellectual structures. "
            "Diffs and merges are line-level, not concept-level. No "
            "typed relationships between repositories. No distinction "
            "between a refinement and a divergence. No expert review "
            "in the scholarly sense. No DOIs (without external "
            "integration). Versioning is mechanical, not intellectual."
        ),
        "when_asked": (
            "If someone says 'How is this different from GitHub?' — "
            "say: 'We love GitHub — it's the inspiration for treating "
            "knowledge with the same rigor as code. But GitHub tracks "
            "line-level changes to files. NodeRail tracks the "
            "intellectual evolution of ideas — refinement, extension, "
            "divergence, split, merge. Our review process evaluates "
            "rigor and novelty, not whether the code compiles. And "
            "our output is a DOI-backed knowledge artifact, not a "
            "repository. Think of NodeRail as GitHub for research "
            "structures, not for source code.'"
        ),
    },

    "google_docs": {
        "differentiator": (
            "Google Docs is where you write. NodeRail is where your "
            "writing becomes a structured, citable contribution."
        ),
        "does_well": (
            "Ubiquitous real-time collaboration. Comments, suggestions, "
            "version history. Zero learning curve. Free for anyone "
            "with a Google account."
        ),
        "lacks": (
            "A document is just a document. No structure beyond "
            "headings and paragraphs. No typed relationships. No "
            "status progression. No expert review workflow. No DOIs. "
            "No lineage. No way to distinguish a mature, validated "
            "framework from a rough draft. Collaboration is great; "
            "publication and permanence are nonexistent."
        ),
        "when_asked": (
            "If someone says 'How is this different from Google Docs?' "
            "— say: 'Google Docs is for writing documents. NodeRail "
            "is for building knowledge structures. A Google Doc has no "
            "type, no status, no relationships to other work, no "
            "review process, and no DOI. NodeRail doesn't replace "
            "your writing tool — it gives your finished thinking a "
            "permanent, structured, citable home.'"
        ),
    },

    "zenodo": {
        "differentiator": (
            "Zenodo stores and issues DOIs. NodeRail builds the "
            "reviewed, interconnected knowledge that earns them."
        ),
        "does_well": (
            "Reliable, CERN-backed DOI issuance for any research "
            "output. Open access. Integrates with GitHub. Trusted "
            "by the academic community for data archiving."
        ),
        "lacks": (
            "Zenodo is a deposit box — you upload a file, get a DOI, "
            "done. No structured knowledge objects. No typed "
            "relationships. No version lineage beyond 'new version of "
            "same deposit.' No expert review. No graph of connected "
            "ideas. No quality signal. Anyone can get a DOI for "
            "anything, which means Zenodo DOIs carry no implicit "
            "credibility."
        ),
        "when_asked": (
            "If someone says 'How is this different from Zenodo?' — "
            "say: 'We actually use Zenodo for DOI issuance — it's "
            "excellent infrastructure. The difference is what happens "
            "before the DOI. On Zenodo, you upload a file and get an "
            "identifier. On NodeRail, you build a structured knowledge "
            "object, connect it to related work, track its evolution, "
            "submit it for expert review, and only then does it earn "
            "a DOI. Our DOIs carry a quality signal because they're "
            "gated by review. Zenodo is our backend; NodeRail is the "
            "intellectual process.'"
        ),
    },

    "traditional_journals": {
        "differentiator": (
            "Journals publish static papers after months of gatekeeping. "
            "NodeRail publishes living structures with continuous "
            "validation."
        ),
        "does_well": (
            "Established credibility. Peer review (however flawed) is "
            "a recognized quality signal. Impact factors, indexing, "
            "tenure considerations. Deep institutional integration."
        ),
        "lacks": (
            "Glacial publication timelines (months to years). Paper "
            "as the atomic unit — ideas that span multiple papers have "
            "no unified representation. Peer review is opaque, slow, "
            "and binary (accept/reject). No version lineage after "
            "publication. No typed relationships between papers. No "
            "graph of knowledge. No API access to structured content. "
            "Locked behind paywalls. The format hasn't evolved since "
            "the 17th century."
        ),
        "when_asked": (
            "If someone says 'Why not just publish in a journal?' — "
            "say: 'Journals are great for the final, polished artifact "
            "— and we're not trying to replace them for tenure "
            "purposes. But most intellectual work never becomes a "
            "journal paper. It's the concept you refine over years, "
            "the measurement instrument you build iteratively, the "
            "framework that evolves through application. That work "
            "deserves to be structured, reviewed, and citable too. "
            "NodeRail publishes the living body of thought. Journals "
            "publish the snapshot.'"
        ),
    },
}


# ===================================================================
# POSITIONING MATRIX — Quick Reference
# ===================================================================

POSITIONING_MATRIX = {
    "header": [
        "Competitor",
        "Their Strength",
        "Their Gap",
        "NodeRail Advantage",
    ],
    "rows": [
        (
            "Notion",
            "Flexible workspace",
            "No scholarly identity",
            "Typed structures + DOIs",
        ),
        (
            "Obsidian",
            "Local-first linking",
            "Untyped, no review",
            "Semantic relationships + validation",
        ),
        (
            "Roam Research",
            "Networked ideation",
            "No publication path",
            "Exploratory-to-canonical pipeline",
        ),
        (
            "ResearchGate",
            "Academic social network",
            "Paper-centric, no structure",
            "Idea-level structures + lineage",
        ),
        (
            "GitHub",
            "Version control + collaboration",
            "Code-oriented, not knowledge",
            "Intellectual versioning + expert review",
        ),
        (
            "Google Docs",
            "Real-time co-editing",
            "No structure or permanence",
            "Structured objects + DOI permanence",
        ),
        (
            "Zenodo",
            "Reliable DOI issuance",
            "Deposit box, no quality gate",
            "Review-gated DOIs with lineage",
        ),
        (
            "Journals",
            "Institutional credibility",
            "Slow, static, siloed",
            "Living structures, continuous review",
        ),
    ],
}


# ===================================================================
# CATEGORY POSITIONING STATEMENT
# ===================================================================

POSITIONING_STATEMENT = (
    "For researchers, field founders, and institutions who need their "
    "intellectual work to be structured, validated, and permanently "
    "citable, NodeRail is a structured research publishing platform "
    "that treats knowledge as a living graph of typed, evolving objects "
    "with expert review and DOI issuance. Unlike note-taking tools that "
    "stop at organization, document repositories that stop at storage, "
    "and journals that stop at static publication, NodeRail provides "
    "the full lifecycle from exploratory idea to canonical, "
    "DOI-backed artifact."
)
