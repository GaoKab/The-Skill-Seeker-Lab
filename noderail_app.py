"""
NodeRail — A structured research environment for building,
connecting, and evolving bodies of thought.

Establish concepts. Track their evolution. Protect their lineage.
"""

import streamlit as st
import streamlit.components.v1 as components

from noderail.models import (
    Node, Edge, Version,
    NODE_TYPES, RELATIONSHIP_TYPES, EVOLUTION_TYPES, STATUS_LEVELS,
    _now,
)
from noderail.storage import NodeRailStore
from noderail.graph_utils import build_graph_html, build_lineage_html
from noderail.export import (
    export_node_markdown,
    export_graph_markdown,
    export_graph_html,
    export_graph_json,
)


# --- Page Config ---

st.set_page_config(
    page_title="NodeRail",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --- Custom CSS ---

st.markdown("""
<style>
    /* Global tone — dark, disciplined, minimal */
    .stApp {
        background-color: #0E1117;
    }
    section[data-testid="stSidebar"] {
        background-color: #0A0D12;
        border-right: 1px solid #1A1D24;
    }
    h1, h2, h3 {
        letter-spacing: 0.5px;
    }
    .node-type-badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 4px;
        font-size: 11px;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-weight: 600;
    }
    .status-badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 3px;
        font-size: 10px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    /* Tone down Streamlit defaults */
    .stButton > button {
        border-radius: 4px;
        letter-spacing: 0.5px;
    }
    div[data-testid="stMetric"] {
        background: #141820;
        border: 1px solid #1E2230;
        border-radius: 8px;
        padding: 12px;
    }
</style>
""", unsafe_allow_html=True)


# --- Initialize Store ---

@st.cache_resource
def get_store():
    return NodeRailStore()

store = get_store()


# --- Sidebar Navigation ---

st.sidebar.markdown("### ◆ NodeRail")
st.sidebar.markdown(
    "<span style='color:#666; font-size:12px; letter-spacing:1px;'>"
    "PUBLISHING SYSTEM FOR LIVING KNOWLEDGE</span>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Establish", "Connect", "Evolve", "Explore", "Workspace", "Insights", "Publish", "Canon"],
    label_visibility="collapsed",
)

# Sidebar stats
stats = store.stats()
if stats["total_nodes"] > 0:
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        f"<span style='color:#555; font-size:11px;'>"
        f"{stats['total_nodes']} nodes · {stats['total_edges']} connections · "
        f"{stats['total_versions']} versions</span>",
        unsafe_allow_html=True,
    )


# ===========================================================================
# HOME
# ===========================================================================

if page == "Home":
    st.markdown("")
    st.markdown("")

    # Hero
    st.markdown(
        "<h1 style='font-size:2.8em; font-weight:300; letter-spacing:1px; "
        "margin-bottom:0;'>Publish living knowledge.</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='font-size:1.15em; color:#888; margin-top:8px; "
        "line-height:1.6; max-width:700px;'>"
        "NodeRail is a publishing system for evolving frameworks, research, "
        "and concepts — built to preserve lineage, attribution, and version "
        "history as your thinking grows."
        "</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='font-size:0.9em; color:#555; margin-top:4px;'>"
        "Not static documents. Not scattered notes. "
        "A structured home for knowledge that keeps developing."
        "</p>",
        unsafe_allow_html=True,
    )

    st.markdown("")
    st.markdown("")

    # What this is
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### What you do here")
        st.markdown("""
        **Establish** — Start a concept. Extend a framework.
        Open an inquiry. Create structured units of intellectual work.

        **Connect** — Define how structures relate: what derives from what,
        what extends, challenges, applies, or diverges.

        **Evolve** — Track how work changes over time. Every refinement,
        extension, reinterpretation, application, and divergence is recorded.

        **Explore** — Navigate the living graph of your conceptual work
        and its connections.

        **Canon** — Publish stable, authoritative versions of your
        most important structures.
        """)

    with col2:
        st.markdown("#### What this is not")
        st.markdown("""
        This is not a note-taking app.
        This is not a document editor.
        This is not a wiki.

        NodeRail is a **publishing system for living knowledge** —
        for researchers, theorists, systems thinkers, founders with
        original frameworks, and writers building intellectual lineage.

        Every unit of work here has **provenance**, **structure**,
        and **tracked evolution**. Your thinking doesn't just get saved.
        It gets *versioned, connected, and preserved*.
        """)

    st.markdown("---")

    # Quick stats
    if stats["total_nodes"] > 0:
        st.markdown("#### Current state")
        cols = st.columns(6)
        type_labels = {
            "concept": "Concepts", "framework": "Frameworks",
            "measurement": "Measurements", "field_note": "Field Notes",
            "inquiry": "Inquiries", "project": "Projects",
        }
        for i, (key, label) in enumerate(type_labels.items()):
            cols[i].metric(label, stats["by_type"].get(key, 0))

        st.markdown("")

        # Show the graph if there's data
        nodes = store.get_all_nodes()
        edges = store.get_all_edges()
        if nodes:
            st.markdown("#### Knowledge graph")
            html = build_graph_html(nodes, edges, height="400px")
            components.html(html, height=420, scrolling=False)
    else:
        st.markdown("")
        st.info(
            "Your graph is empty. Go to **Establish** to create "
            "your first unit of work."
        )


# ===========================================================================
# ESTABLISH
# ===========================================================================

elif page == "Establish":
    st.markdown("## Establish")
    st.markdown(
        "<span style='color:#888;'>Create a new unit of intellectual work.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    # Type selection with descriptions
    st.markdown("#### What are you establishing?")

    type_keys = [t[0] for t in NODE_TYPES]
    type_labels = [t[1] for t in NODE_TYPES]
    type_descs = {t[0]: t[2] for t in NODE_TYPES}

    selected_type = st.selectbox(
        "Type",
        type_keys,
        format_func=lambda x: dict(zip(type_keys, type_labels))[x],
        label_visibility="collapsed",
    )

    st.markdown(
        f"<span style='color:#666; font-size:13px;'>{type_descs[selected_type]}</span>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Type-specific prompts
    TYPE_PROMPTS = {
        "concept": {
            "title_hint": "Name this concept precisely",
            "desc_label": "Definition",
            "desc_hint": "What does this refer to? Why does it matter? What distinguishes it?",
        },
        "framework": {
            "title_hint": "Name this framework",
            "desc_label": "Architecture",
            "desc_hint": "What does this organize? What problem does it help structure? What are its components?",
        },
        "measurement": {
            "title_hint": "Name this measurement or metric",
            "desc_label": "Specification",
            "desc_hint": "What does this assess or indicate? How is it observed or quantified?",
        },
        "field_note": {
            "title_hint": "Title this observation",
            "desc_label": "Observation",
            "desc_hint": "What was observed? Why might it matter? What context produced this?",
        },
        "inquiry": {
            "title_hint": "State the question or tension",
            "desc_label": "The unresolved question",
            "desc_hint": "What remains unresolved? What makes this worth investigating?",
        },
        "project": {
            "title_hint": "Name this project or initiative",
            "desc_label": "Purpose",
            "desc_hint": "What is being built, tested, or applied? What intellectual work does it operationalize?",
        },
    }

    prompts = TYPE_PROMPTS.get(selected_type, TYPE_PROMPTS["concept"])

    # Creation form
    with st.form("establish_form", clear_on_submit=True):
        title = st.text_input("Title", placeholder=prompts["title_hint"])
        description = st.text_area(
            prompts["desc_label"],
            placeholder=prompts["desc_hint"],
            height=150,
        )
        tags_input = st.text_input(
            "Tags",
            placeholder="Comma-separated (e.g., cognition, capacity, measurement)",
        )

        # Initial status
        status = st.selectbox(
            "Initial status",
            [s[0] for s in STATUS_LEVELS[:3]],  # exploratory, developing, stable
            format_func=lambda x: dict((s[0], s[1]) for s in STATUS_LEVELS)[x],
        )

        # Optional: connect on creation
        st.markdown("")
        st.markdown(
            "<span style='color:#888; font-size:13px;'>"
            "Does this derive from, extend, challenge, or apply an existing structure?</span>",
            unsafe_allow_html=True,
        )

        existing_nodes = store.get_all_nodes()
        connect_to = None
        connect_rel = None

        if existing_nodes:
            node_options = {n.id: f"{n.title} ({n.node_type})" for n in existing_nodes}
            connect_to = st.selectbox(
                "Connect to",
                [None] + list(node_options.keys()),
                format_func=lambda x: "— None (standalone) —" if x is None else node_options[x],
            )
            if connect_to:
                rel_keys = [r[0] for r in RELATIONSHIP_TYPES]
                rel_labels = [r[1] for r in RELATIONSHIP_TYPES]
                connect_rel = st.selectbox(
                    "Relationship",
                    rel_keys,
                    format_func=lambda x: dict(zip(rel_keys, rel_labels))[x],
                )

        submitted = st.form_submit_button("Establish", type="primary")

        if submitted and title.strip():
            tags = [t.strip() for t in tags_input.split(",") if t.strip()] if tags_input else []
            node = Node(
                title=title.strip(),
                description=description.strip(),
                node_type=selected_type,
                status=status,
                tags=tags,
            )
            store.add_node(node)

            if connect_to and connect_rel:
                edge = Edge(
                    source_id=node.id,
                    target_id=connect_to,
                    relationship=connect_rel,
                )
                store.add_edge(edge)

            st.session_state["last_created_node_id"] = node.id
            st.rerun()
        elif submitted:
            st.warning("A title is required.")

    # Post-creation: show the object in structural context
    if "last_created_node_id" in st.session_state:
        created_id = st.session_state.pop("last_created_node_id")
        node = store.get_node(created_id)
        if node:
            st.markdown("---")
            type_label = dict((t[0], t[1]) for t in NODE_TYPES).get(node.node_type, node.node_type)
            st.success(f"Established: **{node.title}** ({type_label})")

            # Show it in the graph immediately
            all_nodes = store.get_all_nodes()
            all_edges = store.get_all_edges()
            if all_nodes:
                st.markdown(
                    "<span style='color:#666; font-size:11px; letter-spacing:1px; "
                    "text-transform:uppercase;'>YOUR STRUCTURE IN CONTEXT</span>",
                    unsafe_allow_html=True,
                )
                html = build_graph_html(
                    all_nodes, all_edges,
                    highlight_node_id=created_id,
                    height="350px",
                )
                components.html(html, height=370, scrolling=False)

            # Show connections if any
            connected = store.get_connected_nodes(node.id)
            if connected:
                for other, edge in connected:
                    rel_label = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES).get(
                        edge.relationship, edge.relationship
                    )
                    st.markdown(f"  → *{rel_label}* **{other.title}**")

            # Inline next actions
            st.markdown("")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown(
                    "<span style='color:#888; font-size:12px;'>"
                    "This structure now has a history. You can "
                    "**connect** it to other work or **evolve** it anytime.</span>",
                    unsafe_allow_html=True,
                )


# ===========================================================================
# CONNECT
# ===========================================================================

elif page == "Connect":
    st.markdown("## Connect")
    st.markdown(
        "<span style='color:#888;'>"
        "Define how structures relate to each other.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    nodes = store.get_all_nodes()

    if len(nodes) < 2:
        st.info("You need at least two established structures to create a connection.")
    else:
        node_options = {n.id: f"{n.title} ({n.node_type})" for n in nodes}

        with st.form("connect_form", clear_on_submit=True):
            col1, col2, col3 = st.columns([2, 1, 2])

            with col1:
                source_id = st.selectbox(
                    "Source",
                    list(node_options.keys()),
                    format_func=lambda x: node_options[x],
                )

            with col2:
                rel_keys = [r[0] for r in RELATIONSHIP_TYPES]
                rel_labels = [r[1] for r in RELATIONSHIP_TYPES]
                relationship = st.selectbox(
                    "Relationship",
                    rel_keys,
                    format_func=lambda x: dict(zip(rel_keys, rel_labels))[x],
                )

            with col3:
                target_id = st.selectbox(
                    "Target",
                    list(node_options.keys()),
                    format_func=lambda x: node_options[x],
                )

            description = st.text_input(
                "Context",
                placeholder="Optional: describe why this connection exists",
            )

            submitted = st.form_submit_button("Create connection", type="primary")

            if submitted:
                if source_id == target_id:
                    st.warning("A structure cannot connect to itself.")
                else:
                    edge = Edge(
                        source_id=source_id,
                        target_id=target_id,
                        relationship=relationship,
                        description=description.strip(),
                    )
                    store.add_edge(edge)
                    source_name = node_options[source_id]
                    target_name = node_options[target_id]
                    rel_label = dict(zip(rel_keys, rel_labels))[relationship]
                    st.success(f"Connected: **{source_name}** → {rel_label} → **{target_name}**")
                    st.rerun()

        # Show existing connections
        st.markdown("---")
        st.markdown("#### Existing connections")
        edges = store.get_all_edges()
        if edges:
            for edge in edges:
                src = store.get_node(edge.source_id)
                tgt = store.get_node(edge.target_id)
                if src and tgt:
                    rel_label = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES).get(
                        edge.relationship, edge.relationship
                    )
                    st.markdown(
                        f"**{src.title}** → *{rel_label}* → **{tgt.title}**"
                        + (f"  \n<span style='color:#666; font-size:12px;'>{edge.description}</span>" if edge.description else ""),
                        unsafe_allow_html=True,
                    )
        else:
            st.markdown("<span style='color:#555;'>No connections yet.</span>", unsafe_allow_html=True)


# ===========================================================================
# EVOLVE
# ===========================================================================

elif page == "Evolve":
    st.markdown("## Evolve")
    st.markdown(
        "<span style='color:#888;'>"
        "Track how your work changes. Every evolution is recorded.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    nodes = store.get_all_nodes()

    if not nodes:
        st.info("No structures to evolve yet. Go to **Establish** first.")
    else:
        node_options = {n.id: f"{n.title} (v{n.current_version}, {n.status})" for n in nodes}
        selected_node_id = st.selectbox(
            "Select structure to evolve",
            list(node_options.keys()),
            format_func=lambda x: node_options[x],
        )

        node = store.get_node(selected_node_id)
        if node:
            # Show current state
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            col1.metric("Current version", f"v{node.current_version}")
            col2.metric("Status", node.status.title())
            col3.metric("Type", node.node_type.replace("_", " ").title())

            st.markdown(f"**{node.title}**")
            st.markdown(f"<span style='color:#AAA;'>{node.description}</span>", unsafe_allow_html=True)

            # Version history
            versions = store.get_versions_for_node(node.id)
            if versions:
                st.markdown("")
                lineage_html = build_lineage_html(node, versions)
                components.html(lineage_html, height=120, scrolling=False)

            # Evolution form
            st.markdown("---")
            st.markdown("#### What changed?")
            st.markdown(
                "<span style='color:#888; font-size:13px;'>"
                "Is this a refinement, extension, reinterpretation, "
                "application, divergence, split, or merge?</span>",
                unsafe_allow_html=True,
            )

            with st.form("evolve_form", clear_on_submit=True):
                evo_keys = [e[0] for e in EVOLUTION_TYPES]
                evo_labels = [e[1] for e in EVOLUTION_TYPES]
                evo_descs = {e[0]: e[2] for e in EVOLUTION_TYPES}

                evolution_type = st.selectbox(
                    "Evolution type",
                    evo_keys,
                    format_func=lambda x: dict(zip(evo_keys, evo_labels))[x],
                )
                st.markdown(
                    f"<span style='color:#666; font-size:12px;'>{evo_descs[evolution_type]}</span>",
                    unsafe_allow_html=True,
                )

                new_title = st.text_input("Updated title", value=node.title)
                new_description = st.text_area(
                    "Updated description",
                    value=node.description,
                    height=120,
                )
                changes = st.text_area(
                    "What specifically changed?",
                    placeholder="Describe the change and why it was made.",
                    height=80,
                )

                # Optionally update status
                new_status = st.selectbox(
                    "Status",
                    [s[0] for s in STATUS_LEVELS],
                    format_func=lambda x: dict((s[0], s[1]) for s in STATUS_LEVELS)[x],
                    index=[s[0] for s in STATUS_LEVELS].index(node.status),
                )

                submitted = st.form_submit_button("Record evolution", type="primary")

                if submitted and changes.strip():
                    new_version_num = node.current_version + 1
                    version = Version(
                        node_id=node.id,
                        version_number=new_version_num,
                        evolution_type=evolution_type,
                        title=new_title.strip(),
                        description=new_description.strip(),
                        changes=changes.strip(),
                    )
                    store.add_version(version)

                    # Update the node itself
                    node.title = new_title.strip()
                    node.description = new_description.strip()
                    node.status = new_status
                    node.current_version = new_version_num
                    node.updated_at = _now()
                    store.update_node(node)

                    st.success(
                        f"Recorded: **{node.title}** → v{new_version_num} "
                        f"({evolution_type})"
                    )
                    st.rerun()
                elif submitted:
                    st.warning("Describe what changed before recording.")


# ===========================================================================
# EXPLORE
# ===========================================================================

elif page == "Explore":
    st.markdown("## Explore")
    st.markdown(
        "<span style='color:#888;'>"
        "Navigate the living graph of your conceptual work.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    nodes = store.get_all_nodes()
    edges = store.get_all_edges()

    if not nodes:
        st.info("Your graph is empty. Go to **Establish** to begin.")
    else:
        # Filters
        col1, col2 = st.columns(2)
        with col1:
            filter_type = st.multiselect(
                "Filter by type",
                [t[0] for t in NODE_TYPES],
                format_func=lambda x: dict((t[0], t[1]) for t in NODE_TYPES)[x],
                default=[t[0] for t in NODE_TYPES],
            )
        with col2:
            filter_status = st.multiselect(
                "Filter by status",
                [s[0] for s in STATUS_LEVELS],
                format_func=lambda x: dict((s[0], s[1]) for s in STATUS_LEVELS)[x],
                default=[s[0] for s in STATUS_LEVELS],
            )

        # Filter
        filtered_nodes = [
            n for n in nodes
            if n.node_type in filter_type and n.status in filter_status
        ]
        filtered_ids = {n.id for n in filtered_nodes}
        filtered_edges = [
            e for e in edges
            if e.source_id in filtered_ids and e.target_id in filtered_ids
        ]

        # Graph
        if filtered_nodes:
            html = build_graph_html(filtered_nodes, filtered_edges, height="500px")
            components.html(html, height=520, scrolling=False)

            # Legend
            st.markdown("")
            legend_cols = st.columns(len(NODE_TYPES))
            type_colors = {
                "concept": "#4A6FA5", "framework": "#6B4C9A",
                "measurement": "#2E7D6F", "field_note": "#8B6914",
                "inquiry": "#A0522D", "project": "#555555",
            }
            for i, (key, label, _) in enumerate(NODE_TYPES):
                color = type_colors.get(key, "#888")
                legend_cols[i].markdown(
                    f"<span style='color:{color}; font-size:20px;'>●</span> "
                    f"<span style='color:#AAA; font-size:12px;'>{label}</span>",
                    unsafe_allow_html=True,
                )
        else:
            st.info("No structures match the current filters.")

        # Node detail view — 5-question object anatomy
        st.markdown("---")
        st.markdown("#### Inspect structure")

        node_options = {n.id: n.title for n in filtered_nodes}
        if node_options:
            selected_id = st.selectbox(
                "Select a structure",
                list(node_options.keys()),
                format_func=lambda x: node_options[x],
                label_visibility="collapsed",
            )

            node = store.get_node(selected_id)
            if node:
                type_label = dict((t[0], t[1]) for t in NODE_TYPES).get(node.node_type, node.node_type)
                status_label = dict((s[0], s[1]) for s in STATUS_LEVELS).get(node.status, node.status)

                # A. What is this?
                st.markdown(
                    f"<div style='border-left:3px solid #4A6FA5; padding-left:12px; margin:12px 0;'>"
                    f"<span style='color:#666; font-size:11px; letter-spacing:1px; "
                    f"text-transform:uppercase;'>WHAT IS THIS</span><br>"
                    f"<span style='font-size:1.3em; font-weight:500;'>{node.title}</span><br>"
                    f"<span style='color:#888; font-size:13px;'>{type_label} · Created {node.created_at[:10]}</span>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

                # B. What is its current status?
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Status", status_label)
                col2.metric("Version", f"v{node.current_version}")
                col3.metric("Type", type_label)
                col4.metric("Tags", ", ".join(node.tags) if node.tags else "—")

                # Core definition
                st.markdown("")
                st.markdown(node.description)

                # C. Where did it come from? (upstream lineage)
                upstream = store.get_lineage(node.id)
                incoming = [
                    (other, edge) for other, edge in store.get_connected_nodes(node.id)
                    if edge.target_id == node.id
                ]
                if upstream or incoming:
                    st.markdown("")
                    st.markdown(
                        "<span style='color:#666; font-size:11px; letter-spacing:1px; "
                        "text-transform:uppercase;'>WHERE IT CAME FROM</span>",
                        unsafe_allow_html=True,
                    )
                    shown = set()
                    for other, edge in upstream:
                        if other.id not in shown:
                            rel_label = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES).get(
                                edge.relationship, edge.relationship
                            )
                            st.markdown(f"  ← *{rel_label}* **{other.title}** ({other.node_type})")
                            shown.add(other.id)
                    for other, edge in incoming:
                        if other.id not in shown:
                            rel_label = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES).get(
                                edge.relationship, edge.relationship
                            )
                            st.markdown(f"  ← *{rel_label}* **{other.title}** ({other.node_type})")
                            shown.add(other.id)

                # D. What has it become? (downstream influence)
                outgoing = [
                    (other, edge) for other, edge in store.get_connected_nodes(node.id)
                    if edge.source_id == node.id
                ]
                if outgoing:
                    st.markdown("")
                    st.markdown(
                        "<span style='color:#666; font-size:11px; letter-spacing:1px; "
                        "text-transform:uppercase;'>WHAT IT INFLUENCED</span>",
                        unsafe_allow_html=True,
                    )
                    for other, edge in outgoing:
                        rel_label = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES).get(
                            edge.relationship, edge.relationship
                        )
                        st.markdown(f"  → *{rel_label}* **{other.title}** ({other.node_type})")

                # E. What changed over time? (evolution log)
                versions = store.get_versions_for_node(node.id)
                if versions:
                    st.markdown("")
                    st.markdown(
                        "<span style='color:#666; font-size:11px; letter-spacing:1px; "
                        "text-transform:uppercase;'>EVOLUTION</span>",
                        unsafe_allow_html=True,
                    )
                    lineage_html = build_lineage_html(node, versions)
                    components.html(lineage_html, height=120, scrolling=False)

                    if len(versions) > 1:
                        with st.expander("Full version history"):
                            for v in reversed(versions):
                                evo_label = dict((e[0], e[1]) for e in EVOLUTION_TYPES).get(
                                    v.evolution_type, v.evolution_type
                                )
                                st.markdown(
                                    f"**v{v.version_number}** — {evo_label}  \n"
                                    f"<span style='color:#888; font-size:13px;'>"
                                    f"{v.changes}</span>  \n"
                                    f"<span style='color:#555; font-size:11px;'>"
                                    f"{v.created_at[:10]}</span>",
                                    unsafe_allow_html=True,
                                )

                # --- Inline actions (Connect + Evolve without leaving) ---
                st.markdown("---")
                act_col1, act_col2 = st.columns(2)

                # Inline quick-connect
                with act_col1:
                    st.markdown(
                        "<span style='color:#666; font-size:11px; letter-spacing:1px; "
                        "text-transform:uppercase;'>QUICK CONNECT</span>",
                        unsafe_allow_html=True,
                    )
                    other_nodes = [n for n in filtered_nodes if n.id != node.id]
                    if other_nodes:
                        with st.form(f"qconnect_{node.id}", clear_on_submit=True):
                            qc_options = {n.id: f"{n.title} ({n.node_type})" for n in other_nodes}
                            qc_target = st.selectbox(
                                "To",
                                list(qc_options.keys()),
                                format_func=lambda x: qc_options[x],
                                key=f"qc_target_{node.id}",
                            )
                            rel_keys = [r[0] for r in RELATIONSHIP_TYPES]
                            rel_labels_map = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES)
                            qc_rel = st.selectbox(
                                "Relationship",
                                rel_keys,
                                format_func=lambda x: rel_labels_map[x],
                                key=f"qc_rel_{node.id}",
                            )
                            if st.form_submit_button("Connect", type="secondary"):
                                edge = Edge(
                                    source_id=node.id,
                                    target_id=qc_target,
                                    relationship=qc_rel,
                                )
                                store.add_edge(edge)
                                st.success(f"Connected → {qc_options[qc_target]}")
                                st.rerun()
                    else:
                        st.markdown(
                            "<span style='color:#555; font-size:12px;'>"
                            "No other structures in current view to connect to.</span>",
                            unsafe_allow_html=True,
                        )

                # Inline quick-evolve
                with act_col2:
                    st.markdown(
                        "<span style='color:#666; font-size:11px; letter-spacing:1px; "
                        "text-transform:uppercase;'>QUICK EVOLVE</span>",
                        unsafe_allow_html=True,
                    )
                    with st.form(f"qevolve_{node.id}", clear_on_submit=True):
                        evo_keys = [e[0] for e in EVOLUTION_TYPES]
                        evo_labels_map = dict((e[0], e[1]) for e in EVOLUTION_TYPES)
                        qe_type = st.selectbox(
                            "Type",
                            evo_keys,
                            format_func=lambda x: evo_labels_map[x],
                            key=f"qe_type_{node.id}",
                        )
                        qe_changes = st.text_input(
                            "What changed?",
                            placeholder="Brief description of what evolved",
                            key=f"qe_changes_{node.id}",
                        )
                        if st.form_submit_button("Record", type="secondary"):
                            if qe_changes.strip():
                                new_ver = node.current_version + 1
                                version = Version(
                                    node_id=node.id,
                                    version_number=new_ver,
                                    evolution_type=qe_type,
                                    title=node.title,
                                    description=node.description,
                                    changes=qe_changes.strip(),
                                )
                                store.add_version(version)
                                node.current_version = new_ver
                                node.updated_at = _now()
                                store.update_node(node)
                                st.success(f"Recorded v{new_ver} ({qe_type})")
                                st.rerun()
                            else:
                                st.warning("Describe what changed.")


# ===========================================================================
# WORKSPACE
# ===========================================================================

elif page == "Workspace":
    st.markdown("## Workspace")
    st.markdown(
        "<span style='color:#888;'>"
        "A filtered working area for active development within a domain.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    nodes = store.get_all_nodes()

    if not nodes:
        st.info("No structures yet. Go to **Establish** to begin.")
    else:
        # Collect all unique tags across nodes
        all_tags = sorted(set(tag for n in nodes for tag in n.tags))

        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            ws_filter_type = st.multiselect(
                "Filter by type",
                [t[0] for t in NODE_TYPES],
                format_func=lambda x: dict((t[0], t[1]) for t in NODE_TYPES)[x],
            )
        with col2:
            ws_filter_status = st.multiselect(
                "Filter by status",
                [s[0] for s in STATUS_LEVELS],
                format_func=lambda x: dict((s[0], s[1]) for s in STATUS_LEVELS)[x],
            )
        with col3:
            ws_filter_tags = st.multiselect(
                "Filter by tags",
                all_tags,
            ) if all_tags else None

        # Apply filters
        ws_nodes = nodes
        if ws_filter_type:
            ws_nodes = [n for n in ws_nodes if n.node_type in ws_filter_type]
        if ws_filter_status:
            ws_nodes = [n for n in ws_nodes if n.status in ws_filter_status]
        if ws_filter_tags:
            ws_nodes = [n for n in ws_nodes if any(t in n.tags for t in ws_filter_tags)]

        if not ws_nodes:
            st.info("No structures match the current filters.")
        else:
            # Show filtered graph
            ws_ids = {n.id for n in ws_nodes}
            ws_edges = [
                e for e in store.get_all_edges()
                if e.source_id in ws_ids and e.target_id in ws_ids
            ]
            if len(ws_nodes) > 1 or ws_edges:
                html = build_graph_html(ws_nodes, ws_edges, height="350px")
                components.html(html, height=370, scrolling=False)

            st.markdown("---")

            # List view
            for node in sorted(ws_nodes, key=lambda n: n.updated_at, reverse=True):
                type_label = dict((t[0], t[1]) for t in NODE_TYPES).get(
                    node.node_type, node.node_type
                )
                status_label = dict((s[0], s[1]) for s in STATUS_LEVELS).get(
                    node.status, node.status
                )

                status_colors = {
                    "exploratory": "#AAAAAA", "developing": "#4A6FA5",
                    "stable": "#2E7D6F", "canonical": "#6B4C9A",
                    "archived": "#666666",
                }
                s_color = status_colors.get(node.status, "#888")

                with st.expander(
                    f"**{node.title}**  —  {type_label} · v{node.current_version}"
                ):
                    st.markdown(
                        f"<span style='color:{s_color}; font-size:11px; "
                        f"letter-spacing:1px; text-transform:uppercase; "
                        f"font-weight:600;'>{status_label}</span>"
                        f"&nbsp;&nbsp;"
                        f"<span style='color:#555; font-size:11px;'>"
                        f"Updated {node.updated_at[:10]}</span>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(node.description)

                    if node.tags:
                        st.markdown(
                            f"<span style='color:#555; font-size:12px;'>"
                            f"Tags: {', '.join(node.tags)}</span>",
                            unsafe_allow_html=True,
                        )

                    # Show connections
                    connected = store.get_connected_nodes(node.id)
                    if connected:
                        conn_strs = []
                        for other, edge in connected:
                            rel_label = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES).get(
                                edge.relationship, edge.relationship
                            )
                            direction = "→" if edge.source_id == node.id else "←"
                            conn_strs.append(f"{direction} *{rel_label}* **{other.title}**")
                        st.markdown(" · ".join(conn_strs))

            st.markdown("")
            st.markdown(
                f"<span style='color:#555; font-size:12px;'>"
                f"Showing {len(ws_nodes)} of {len(nodes)} structures</span>",
                unsafe_allow_html=True,
            )


# ===========================================================================
# INSIGHTS
# ===========================================================================

elif page == "Insights":
    st.markdown("## Insights")
    st.markdown(
        "<span style='color:#888;'>"
        "What your system sees that you might not. Gaps, tensions, "
        "and structures ready to advance.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    analysis = store.run_full_analysis()

    # --- Summary metrics ---
    total_issues = (
        len(analysis["orphaned"])
        + len(analysis["unmeasured_concepts"])
        + len(analysis["unsupported_inquiries"])
        + len(analysis["unoperationalized"])
    )
    total_opportunities = (
        len(analysis["long_exploratory"])
        + len(analysis["contradictions"])
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Structural gaps", total_issues)
    col2.metric("Ready to advance", len(analysis["long_exploratory"]))
    col3.metric("Active tensions", len(analysis["contradictions"]))
    col4.metric("Hub structures", len(analysis["hubs"]))

    st.markdown("---")

    # --- Active Tensions (most intellectually interesting) ---
    st.markdown("#### Active tensions")
    st.markdown(
        "<span style='color:#888; font-size:13px;'>"
        "Structures that challenge each other — unresolved contradictions "
        "in the system.</span>",
        unsafe_allow_html=True,
    )
    if analysis["contradictions"]:
        for src, tgt, edge in analysis["contradictions"]:
            st.markdown(
                f"**{src.title}** ({src.node_type}) "
                f"*challenges* **{tgt.title}** ({tgt.node_type})"
            )
            if edge.description:
                st.markdown(
                    f"<span style='color:#666; font-size:12px; margin-left:16px;'>"
                    f"{edge.description}</span>",
                    unsafe_allow_html=True,
                )
    else:
        st.markdown(
            "<span style='color:#555;'>No active tensions. "
            "This may mean the system is coherent — or that "
            "challenges haven't been recorded yet.</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # --- Ready to Advance ---
    st.markdown("#### Ready to advance")
    st.markdown(
        "<span style='color:#888; font-size:13px;'>"
        "Structures still marked 'exploratory' but with enough connections "
        "to suggest they've matured beyond that status.</span>",
        unsafe_allow_html=True,
    )
    if analysis["long_exploratory"]:
        for node in analysis["long_exploratory"]:
            edge_count = len(store.get_edges_for_node(node.id))
            type_label = dict(
                (t[0], t[1]) for t in NODE_TYPES
            ).get(node.node_type, node.node_type)
            st.markdown(
                f"**{node.title}** — {type_label} · "
                f"{edge_count} connections · still exploratory"
            )
    else:
        st.markdown(
            "<span style='color:#555;'>No structures ready to advance.</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # --- Unmeasured Concepts ---
    st.markdown("#### Unmeasured concepts")
    st.markdown(
        "<span style='color:#888; font-size:13px;'>"
        "Concepts with no measurement connected. If a concept matters, "
        "how would you observe or quantify it?</span>",
        unsafe_allow_html=True,
    )
    if analysis["unmeasured_concepts"]:
        for node in analysis["unmeasured_concepts"]:
            st.markdown(f"**{node.title}**")
    else:
        st.markdown(
            "<span style='color:#555;'>All concepts have at least "
            "one measurement connected.</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # --- Unsupported Inquiries ---
    st.markdown("#### Inquiries without field evidence")
    st.markdown(
        "<span style='color:#888; font-size:13px;'>"
        "Open questions with no field notes feeding into them. "
        "These inquiries are purely theoretical — no grounded "
        "observations yet.</span>",
        unsafe_allow_html=True,
    )
    if analysis["unsupported_inquiries"]:
        for node in analysis["unsupported_inquiries"]:
            st.markdown(f"**{node.title}**")
    else:
        st.markdown(
            "<span style='color:#555;'>All inquiries have supporting "
            "field notes.</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # --- Unoperationalized Frameworks ---
    st.markdown("#### Frameworks without projects")
    st.markdown(
        "<span style='color:#888; font-size:13px;'>"
        "Frameworks that no project operationalizes. Theory without "
        "application — is that intentional?</span>",
        unsafe_allow_html=True,
    )
    if analysis["unoperationalized"]:
        for node in analysis["unoperationalized"]:
            st.markdown(f"**{node.title}**")
    else:
        st.markdown(
            "<span style='color:#555;'>All frameworks have at least "
            "one project operationalizing them.</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # --- Orphaned Nodes ---
    st.markdown("#### Orphaned structures")
    st.markdown(
        "<span style='color:#888; font-size:13px;'>"
        "Structures with zero connections — completely isolated "
        "from the graph.</span>",
        unsafe_allow_html=True,
    )
    if analysis["orphaned"]:
        for node in analysis["orphaned"]:
            type_label = dict(
                (t[0], t[1]) for t in NODE_TYPES
            ).get(node.node_type, node.node_type)
            st.markdown(f"**{node.title}** — {type_label}")
    else:
        st.markdown(
            "<span style='color:#2E7D6F;'>No orphaned structures. "
            "Everything is connected.</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # --- Stale structures ---
    stale = analysis["stale"]
    if stale:
        with st.expander(
            f"Stale structures — {len(stale)} still at v1 (never evolved)"
        ):
            for node in stale:
                type_label = dict(
                    (t[0], t[1]) for t in NODE_TYPES
                ).get(node.node_type, node.node_type)
                st.markdown(
                    f"**{node.title}** — {type_label} · {node.status}"
                )

    # --- Hubs ---
    st.markdown("#### Knowledge hubs")
    st.markdown(
        "<span style='color:#888; font-size:13px;'>"
        "The most connected structures in your graph — "
        "where intellectual weight concentrates.</span>",
        unsafe_allow_html=True,
    )
    if analysis["hubs"]:
        for node, count in analysis["hubs"]:
            type_label = dict(
                (t[0], t[1]) for t in NODE_TYPES
            ).get(node.node_type, node.node_type)
            bar_width = min(count * 8, 100)
            st.markdown(
                f"**{node.title}** — {type_label} · "
                f"{count} connections"
            )
            st.markdown(
                f"<div style='background:#1E2230; border-radius:4px; "
                f"height:8px; width:100%; margin-bottom:12px;'>"
                f"<div style='background:#4A6FA5; border-radius:4px; "
                f"height:8px; width:{bar_width}%;'></div></div>",
                unsafe_allow_html=True,
            )
    else:
        st.markdown(
            "<span style='color:#555;'>No hub structures yet "
            "(need 5+ connections).</span>",
            unsafe_allow_html=True,
        )


# ===========================================================================
# PUBLISH
# ===========================================================================

elif page == "Publish":
    st.markdown("## Publish")
    st.markdown(
        "<span style='color:#888;'>"
        "Export your intellectual work as shareable artifacts.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    nodes = store.get_all_nodes()

    if not nodes:
        st.info("No structures to publish. Go to **Establish** first.")
    else:
        publish_tab1, publish_tab2, publish_tab3, publish_tab4 = st.tabs([
            "Single Structure", "Full Graph (Markdown)", "Interactive Graph (HTML)", "Raw Data (JSON)"
        ])

        # --- Tab 1: Single structure markdown ---
        with publish_tab1:
            st.markdown(
                "<span style='color:#888; font-size:13px;'>"
                "Export a single structure with its connections, "
                "lineage, and full evolution history.</span>",
                unsafe_allow_html=True,
            )
            st.markdown("")

            _type_label_map = dict((t[0], t[1]) for t in NODE_TYPES)

            node_options = {
                n.id: f"{n.title} ({_type_label_map.get(n.node_type, n.node_type)})"
                for n in sorted(nodes, key=lambda x: x.title)
            }

            selected_id = st.selectbox(
                "Select structure to export",
                list(node_options.keys()),
                format_func=lambda x: node_options[x],
                key="publish_node_select",
            )

            if selected_id:
                md_content = export_node_markdown(store, selected_id)
                node = store.get_node(selected_id)

                # Preview
                with st.expander("Preview", expanded=True):
                    st.markdown(md_content)

                # Download
                st.download_button(
                    label="Download Markdown",
                    data=md_content,
                    file_name=f"noderail_{node.title.lower().replace(' ', '_')}.md",
                    mime="text/markdown",
                )

        # --- Tab 2: Full graph markdown ---
        with publish_tab2:
            st.markdown(
                "<span style='color:#888; font-size:13px;'>"
                "Export the entire knowledge graph as a structured "
                "markdown document — every structure, connection, "
                "and status.</span>",
                unsafe_allow_html=True,
            )
            st.markdown("")

            if st.button("Generate full graph export", key="gen_graph_md"):
                with st.spinner("Generating..."):
                    graph_md = export_graph_markdown(store)

                st.session_state["graph_md"] = graph_md

            if "graph_md" in st.session_state:
                graph_md = st.session_state["graph_md"]

                with st.expander("Preview (first 200 lines)"):
                    preview_lines = graph_md.split("\n")[:200]
                    st.markdown("\n".join(preview_lines))
                    if len(graph_md.split("\n")) > 200:
                        st.markdown("*... truncated for preview ...*")

                st.download_button(
                    label="Download Full Graph Markdown",
                    data=graph_md,
                    file_name="noderail_full_graph.md",
                    mime="text/markdown",
                    key="dl_graph_md",
                )

        # --- Tab 3: Interactive HTML graph ---
        with publish_tab3:
            st.markdown(
                "<span style='color:#888; font-size:13px;'>"
                "Export the knowledge graph as a standalone HTML file "
                "anyone can open in a browser — no server needed.</span>",
                unsafe_allow_html=True,
            )
            st.markdown("")

            if st.button("Generate interactive graph", key="gen_graph_html"):
                with st.spinner("Generating..."):
                    graph_html = export_graph_html(store)

                st.session_state["graph_html"] = graph_html

            if "graph_html" in st.session_state:
                graph_html = st.session_state["graph_html"]

                stats = store.stats()
                st.markdown(
                    f"<span style='color:#555; font-size:12px;'>"
                    f"Generated: {stats['total_nodes']} nodes, "
                    f"{stats['total_edges']} edges, "
                    f"{len(graph_html):,} bytes</span>",
                    unsafe_allow_html=True,
                )

                st.download_button(
                    label="Download Interactive Graph (HTML)",
                    data=graph_html,
                    file_name="noderail_graph.html",
                    mime="text/html",
                    key="dl_graph_html",
                )

        # --- Tab 4: Raw JSON ---
        with publish_tab4:
            st.markdown(
                "<span style='color:#888; font-size:13px;'>"
                "Export the raw graph data as JSON — nodes, edges, "
                "versions. Use this to back up, migrate, or integrate "
                "with other systems.</span>",
                unsafe_allow_html=True,
            )
            st.markdown("")

            if st.button("Generate JSON export", key="gen_json"):
                with st.spinner("Generating..."):
                    json_content = export_graph_json(store)

                st.session_state["json_export"] = json_content

            if "json_export" in st.session_state:
                json_content = st.session_state["json_export"]

                st.markdown(
                    f"<span style='color:#555; font-size:12px;'>"
                    f"{len(json_content):,} bytes</span>",
                    unsafe_allow_html=True,
                )

                with st.expander("Preview"):
                    st.code(json_content[:3000], language="json")
                    if len(json_content) > 3000:
                        st.markdown("*... truncated for preview ...*")

                st.download_button(
                    label="Download JSON",
                    data=json_content,
                    file_name="noderail_export.json",
                    mime="application/json",
                    key="dl_json",
                )


# ===========================================================================
# CANON
# ===========================================================================

elif page == "Canon":
    st.markdown("## Canon")
    st.markdown(
        "<span style='color:#888;'>"
        "Curated, authoritative versions of your most important work.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    canonical = store.get_nodes_by_status("canonical")
    stable = store.get_nodes_by_status("stable")

    if not canonical and not stable:
        st.markdown("""
        No canonical or stable structures yet.

        To elevate work to canon:
        1. Go to **Evolve**
        2. Select a structure
        3. Set its status to **Canonical**

        Canon represents your most mature, authoritative work —
        the structures you stand behind as definitive.
        """)
    else:
        if canonical:
            st.markdown("#### Canonical")
            st.markdown(
                "<span style='color:#666; font-size:12px;'>"
                "Authoritative. Curated. Definitive.</span>",
                unsafe_allow_html=True,
            )
            st.markdown("")
            for node in canonical:
                type_label = dict((t[0], t[1]) for t in NODE_TYPES).get(node.node_type, node.node_type)
                with st.expander(f"◆ {node.title}  —  {type_label}, v{node.current_version}"):
                    st.markdown(node.description)
                    if node.tags:
                        st.markdown(f"*Tags: {', '.join(node.tags)}*")
                    versions = store.get_versions_for_node(node.id)
                    if versions:
                        lineage_html = build_lineage_html(node, versions)
                        components.html(lineage_html, height=120, scrolling=False)

        if stable:
            st.markdown("")
            st.markdown("#### Stable")
            st.markdown(
                "<span style='color:#666; font-size:12px;'>"
                "Mature. Unlikely to change significantly.</span>",
                unsafe_allow_html=True,
            )
            st.markdown("")
            for node in stable:
                type_label = dict((t[0], t[1]) for t in NODE_TYPES).get(node.node_type, node.node_type)
                with st.expander(f"○ {node.title}  —  {type_label}, v{node.current_version}"):
                    st.markdown(node.description)
                    if node.tags:
                        st.markdown(f"*Tags: {', '.join(node.tags)}*")
                    versions = store.get_versions_for_node(node.id)
                    if versions:
                        lineage_html = build_lineage_html(node, versions)
                        components.html(lineage_html, height=120, scrolling=False)
