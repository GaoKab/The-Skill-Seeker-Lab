"""
NodeRail Competitor Positioning & Messaging (v2)

Strategic reference document. Not executable code.
Rebuilt around the core truth: NodeRail is living knowledge
infrastructure, not a publishing tool.
"""


# ===================================================================
# CATEGORY DEFINITION
# ===================================================================

CATEGORY = {
    "name": "Living Knowledge Infrastructure",
    "definition": (
        "Infrastructure for building, evolving, validating, and preserving "
        "serious knowledge as structured, connected, and attributable work. "
        "Living Knowledge Infrastructure treats ideas not as documents but "
        "as intellectual objects that grow, connect, earn credibility, "
        "and remain permanent."
    ),
    "why_new_category": (
        "Existing tools force false choices: flexible-but-unstructured "
        "(Notion, Obsidian) or rigorous-but-rigid (journals, Zenodo). "
        "None of them treat knowledge as living infrastructure — something "
        "that evolves visibly, maintains lineage, earns validation, and "
        "stays attributed when machines consume it."
    ),
}


# ===================================================================
# THE PROBLEM (lead with this, not explanation)
# ===================================================================

THE_PROBLEM = {
    "headline": "We still build knowledge in systems that fail it.",

    "failures": [
        "Fragment thinking across documents and tools",
        "Erase how ideas evolve over time",
        "Fail to preserve authorship and lineage",
        "Reset progress across people and time",
        "Feed AI flattened, unattributed information",
    ],

    "consequence": (
        "Important knowledge gets lost, misattributed, or consumed "
        "without credit. The lifecycle of a research idea is broken — "
        "from private tool to static paper to PDF graveyard."
    ),
}


# ===================================================================
# THE SHIFT
# ===================================================================

THE_SHIFT = {
    "from": [
        "Documents",
        "Static papers",
        "Disconnected notes",
        "Version history as file diffs",
        "Peer review as gatekeeping",
    ],
    "to": [
        "Structured intellectual objects",
        "Visible lineage",
        "Evolving knowledge systems",
        "Intellectual evolution tracking",
        "Continuous expert validation",
    ],
    "key_insight": (
        "The unit of knowledge should not be the document. "
        "It should be the idea — structured, connected, and evolving."
    ),
}


# ===================================================================
# WHAT NODERAIL ENABLES
# ===================================================================

ENABLES = {
    "continuity": "Work doesn't reset. Ideas survive across people and time.",
    "lineage": "Ideas evolve visibly. Every change is tracked and typed.",
    "legibility": "Others can follow your thinking and build on it.",
    "validation": "Expert review creates a credibility layer.",
    "permanence": "DOI issuance and archival make work citable forever.",
    "trusted_ai_access": "Structured, attributed knowledge for machine consumption.",
}


# ===================================================================
# TAGLINE OPTIONS (tightened)
# ===================================================================

TAGLINES = [
    "Build knowledge that survives.",
    "Where ideas don't disappear.",
    "Structure your thinking. Preserve your work.",
    "Build bodies of thought, not piles of documents.",
    "Your intellectual work deserves infrastructure.",
    "Governed knowledge infrastructure for the AI era.",
]


# ===================================================================
# ELEVATOR PITCHES
# ===================================================================

ELEVATOR_PITCH_30_SEC = (
    "We still build knowledge in systems that fragment it, erase how "
    "it evolves, and strip attribution when AI consumes it. NodeRail "
    "fixes this. It's infrastructure for living knowledge — you create "
    "structured objects like concepts and frameworks, connect them with "
    "meaningful relationships, track their evolution, get them reviewed "
    "by experts, and issue permanent DOIs. When AI accesses your work "
    "through our API, attribution travels with it. NodeRail is where "
    "serious knowledge lives, evolves, and stays yours."
)

ELEVATOR_PITCH_2_MIN = (
    "Right now, the lifecycle of a research idea is broken. You think "
    "in a private tool like Notion or Obsidian, then you write it up "
    "as a static paper, submit it to a journal that takes months to "
    "review, and if it gets published, it sits as a PDF that nobody "
    "can build on programmatically. Meanwhile, AI systems scrape "
    "everything and strip the authorship.\n\n"

    "NodeRail is living knowledge infrastructure. You create typed "
    "structures — a concept, a framework, a measurement instrument — "
    "and connect them with relationships that carry meaning: 'derives "
    "from,' 'extends,' 'challenges.' Every change is tracked as an "
    "evolution: refinement, extension, divergence, split. You're "
    "building lineage, not just version history.\n\n"

    "When the work is mature, you request expert review through the "
    "platform. Reviewers evaluate rigor and novelty using a structured "
    "rubric. If validated, the structure advances to stable status and "
    "receives a DOI — a permanent citable identifier — with the review, "
    "lineage, and connections all embedded in the metadata.\n\n"

    "For institutions, NodeRail is how you see your intellectual output "
    "connect and evolve across labs and departments. For AI developers, "
    "it's an API to structured, expert-reviewed knowledge with "
    "provenance — not scraped web pages.\n\n"

    "We're not a note-taking app. We're not a journal. We're the "
    "infrastructure layer for how knowledge gets built, validated, "
    "and made permanent."
)


# ===================================================================
# COMPETITOR POSITIONING (simplified + stronger)
# ===================================================================

COMPETITOR_ONE_LINERS = {
    "notion": "Notion → organizes work. NodeRail → evolves knowledge.",
    "obsidian": "Obsidian → links notes. NodeRail → structures and validates knowledge.",
    "roam": "Roam → captures thinking. NodeRail → publishes what you've thought.",
    "researchgate": "ResearchGate → shares papers. NodeRail → publishes the living structures underneath them.",
    "github": "GitHub → versions code. NodeRail → versions knowledge.",
    "google_docs": "Google Docs → where you write. NodeRail → where your writing becomes permanent.",
    "zenodo": "Zenodo → stores outputs. NodeRail → builds the reviewed knowledge that earns a DOI.",
    "journals": "Journals → publish snapshots. NodeRail → publishes living structures.",
}

COMPETITORS = {

    "notion": {
        "differentiator": (
            "Notion organizes your work. NodeRail evolves your knowledge — "
            "with typed relationships, lineage tracking, expert validation, "
            "and permanent DOIs."
        ),
        "does_well": (
            "Flexible workspace for teams. Excellent for internal docs, "
            "project management, and lightweight databases. Low friction."
        ),
        "lacks": (
            "No concept of intellectual rigor. No typed relationships. "
            "No version lineage. No expert review. No DOIs. No way to "
            "make work citable or permanent. Everything lives in a "
            "proprietary silo with no scholarly identity."
        ),
        "when_asked": (
            "'Notion is a workspace. NodeRail is knowledge infrastructure. "
            "In Notion, you organize pages. In NodeRail, you build "
            "structured intellectual objects with explicit relationships, "
            "evolution tracking, and expert validation. Your work gets a "
            "DOI. Notion will never give your ideas a permanent, citable "
            "identity.'"
        ),
    },

    "obsidian": {
        "differentiator": (
            "Obsidian links your notes. NodeRail structures your "
            "knowledge and makes it citable."
        ),
        "does_well": (
            "Excellent local-first markdown editor. Bidirectional "
            "linking, graph view, plugin ecosystem. Beloved by PKM users."
        ),
        "lacks": (
            "Links are untyped — no distinction between 'extends' and "
            "'challenges.' No version lineage. No expert review. No DOIs. "
            "No institutional layer. The graph looks impressive but "
            "carries no semantic weight."
        ),
        "when_asked": (
            "'Obsidian is a personal knowledge base with links. NodeRail "
            "is a shared environment with typed relationships. Every "
            "connection has meaning — derives from, challenges, "
            "operationalizes. Your work can be reviewed, validated, and "
            "issued a DOI. Obsidian is for thinking. NodeRail is for "
            "publishing what you've thought.'"
        ),
    },

    "roam_research": {
        "differentiator": (
            "Roam captures the process of thinking. NodeRail builds "
            "the structure of knowledge — and makes it permanent."
        ),
        "does_well": (
            "Pioneered networked thought and block-level references. "
            "Strong for brainstorming and associative exploration."
        ),
        "lacks": (
            "Designed for personal ideation, not for publication or "
            "validation. No typed relationships. No status progression. "
            "No review. No DOIs. Knowledge stays informal and private."
        ),
        "when_asked": (
            "'Roam is the messy early phase. NodeRail picks up where "
            "Roam stops. When your thinking has enough shape to be a "
            "concept or framework, NodeRail gives it structure, tracks "
            "its evolution, and lets an expert validate it for a DOI. "
            "Roam is upstream; NodeRail is downstream.'"
        ),
    },

    "researchgate": {
        "differentiator": (
            "ResearchGate shares finished papers. NodeRail publishes "
            "the living structures underneath them."
        ),
        "does_well": (
            "Large academic social network. Good for sharing papers and "
            "finding collaborators."
        ),
        "lacks": (
            "Paper-centric. No structured knowledge objects. No typed "
            "relationships between ideas across papers. No version "
            "lineage. No platform-native review. Essentially a social "
            "network bolted onto a document repository."
        ),
        "when_asked": (
            "'ResearchGate is a social network for sharing papers. "
            "NodeRail is infrastructure for the ideas inside those papers. "
            "A concept spread across five papers has no unified identity "
            "on ResearchGate. On NodeRail, it's a single structure with "
            "its own lineage, connections, reviews, and DOI.'"
        ),
    },

    "github": {
        "differentiator": (
            "GitHub versions code. NodeRail versions knowledge — with "
            "evolution types, expert review, and DOIs."
        ),
        "does_well": (
            "Industry-standard version control. Pull requests, code "
            "review, CI/CD. Trusted collaboration model."
        ),
        "lacks": (
            "Designed for code, not intellectual structures. Diffs are "
            "line-level, not concept-level. No distinction between a "
            "refinement and a divergence. No scholarly review. No DOIs."
        ),
        "when_asked": (
            "'GitHub is the inspiration — we treat knowledge with the "
            "same rigor as code. But GitHub tracks line-level changes to "
            "files. NodeRail tracks intellectual evolution — refinement, "
            "extension, divergence. Our review evaluates rigor and "
            "novelty. Our output is a DOI-backed knowledge artifact. "
            "Think GitHub for research structures, not source code.'"
        ),
    },

    "google_docs": {
        "differentiator": (
            "Google Docs is where you write. NodeRail is where your "
            "writing becomes structured, validated, and permanent."
        ),
        "does_well": (
            "Ubiquitous real-time collaboration. Zero learning curve. "
            "Free."
        ),
        "lacks": (
            "A document is just a document. No structure beyond headings. "
            "No typed relationships. No status progression. No review. "
            "No DOIs. No lineage. No permanence."
        ),
        "when_asked": (
            "'Google Docs is for writing. NodeRail is for building "
            "knowledge structures. A doc has no type, no status, no "
            "relationships, no review, and no DOI. NodeRail doesn't "
            "replace your writing tool — it gives your finished thinking "
            "a permanent, structured, citable home.'"
        ),
    },

    "zenodo": {
        "differentiator": (
            "Zenodo stores and issues DOIs. NodeRail builds the "
            "reviewed, interconnected knowledge that earns them."
        ),
        "does_well": (
            "Reliable, CERN-backed DOI issuance. Open access. Trusted "
            "for data archiving."
        ),
        "lacks": (
            "A deposit box. No structured knowledge objects. No typed "
            "relationships. No evolution lineage. No expert review. No "
            "quality signal. Anyone can get a DOI for anything."
        ),
        "when_asked": (
            "'We use Zenodo for DOI issuance — it's excellent. The "
            "difference is what happens before the DOI. On Zenodo, you "
            "upload a file and get an identifier. On NodeRail, you build "
            "a structured object, connect it, track its evolution, get "
            "it reviewed, and only then does it earn a DOI. Our DOIs "
            "carry a quality signal because they're gated by review.'"
        ),
    },

    "traditional_journals": {
        "differentiator": (
            "Journals publish static snapshots after months of gatekeeping. "
            "NodeRail publishes living structures with continuous validation."
        ),
        "does_well": (
            "Established credibility. Peer review as recognized quality "
            "signal. Deep institutional integration."
        ),
        "lacks": (
            "Glacial timelines. Paper as the only unit. Opaque, binary "
            "review. No lineage after publication. No typed relationships. "
            "No knowledge graph. No API. Paywalled. Format unchanged "
            "since the 17th century."
        ),
        "when_asked": (
            "'Journals are for the polished artifact — we're not replacing "
            "them for tenure. But most intellectual work never becomes a "
            "paper. The concept refined over years, the measurement built "
            "iteratively, the framework that evolves through application — "
            "that work deserves to be structured, reviewed, and citable "
            "too. NodeRail publishes the living body of thought. Journals "
            "publish the snapshot.'"
        ),
    },
}


# ===================================================================
# POSITIONING MATRIX — Quick Reference
# ===================================================================

POSITIONING_MATRIX = {
    "header": ["Competitor", "What they do", "What's missing", "NodeRail"],
    "rows": [
        ("Notion", "Organizes work", "No scholarly identity", "Evolves knowledge"),
        ("Obsidian", "Links notes", "Untyped, no review", "Structures + validates"),
        ("Roam", "Captures thinking", "No publication path", "Publishes thinking"),
        ("ResearchGate", "Shares papers", "Paper-centric", "Publishes ideas"),
        ("GitHub", "Versions code", "Not for knowledge", "Versions knowledge"),
        ("Google Docs", "Co-editing", "No permanence", "Permanent structures"),
        ("Zenodo", "Issues DOIs", "No quality gate", "Review-gated DOIs"),
        ("Journals", "Credibility", "Slow, static", "Living structures"),
    ],
}


# ===================================================================
# POSITIONING STATEMENT
# ===================================================================

POSITIONING_STATEMENT = (
    "For researchers, field founders, and institutions who need their "
    "intellectual work to be structured, validated, and permanently "
    "citable, NodeRail is living knowledge infrastructure that treats "
    "ideas as evolving, connected objects with expert review, lineage "
    "tracking, and DOI issuance. Unlike tools that stop at organization, "
    "repositories that stop at storage, and journals that stop at static "
    "publication, NodeRail provides the full lifecycle from exploratory "
    "idea to canonical, DOI-backed artifact — with trusted AI access "
    "built in."
)
