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
    "STRUCTURED RESEARCH ENVIRONMENT</span>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Establish", "Connect", "Evolve", "Explore", "Canon"],
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

    # Creation form
    with st.form("establish_form", clear_on_submit=True):
        title = st.text_input("Title", placeholder="Name this structure")
        description = st.text_area(
            "Description",
            placeholder="Define what this is, what it contains, and why it matters.",
            height=150,
        )
        tags_input = st.text_input(
            "Tags",
            placeholder="Comma-separated (e.g., cognition, capacity, measurement)",
        )

        # Initial status
        status = st.selectbox(
            "Initial status",
            [s[0] for s in STATUS_LEVELS[:3]],  # draft, active, stable
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

            st.success(f"Established: **{node.title}** ({selected_type})")
            st.rerun()
        elif submitted:
            st.warning("A title is required.")


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
                "application, or divergence?</span>",
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

        # Node detail view
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

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Type", type_label)
                col2.metric("Status", status_label)
                col3.metric("Version", f"v{node.current_version}")
                col4.metric("Tags", ", ".join(node.tags) if node.tags else "—")

                st.markdown(f"**{node.title}**")
                st.markdown(node.description)

                # Connections
                connected = store.get_connected_nodes(node.id)
                if connected:
                    st.markdown("")
                    st.markdown("**Connections:**")
                    for other, edge in connected:
                        rel_label = dict((r[0], r[1]) for r in RELATIONSHIP_TYPES).get(
                            edge.relationship, edge.relationship
                        )
                        direction = "→" if edge.source_id == node.id else "←"
                        st.markdown(
                            f"  {direction} *{rel_label}* → **{other.title}** ({other.node_type})"
                        )

                # Lineage
                versions = store.get_versions_for_node(node.id)
                if versions and len(versions) > 1:
                    st.markdown("")
                    lineage_html = build_lineage_html(node, versions)
                    components.html(lineage_html, height=120, scrolling=False)


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
