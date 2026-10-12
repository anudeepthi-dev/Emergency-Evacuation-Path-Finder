import os
import matplotlib.pyplot as plt
import streamlit as st

from algorithms import bfs, ucs, a_star


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Emergency Evacuation Path Finder",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Emergency Evacuation Path Finder")

st.write(
    "Find a safe route to an emergency exit using BFS, "
    "Uniform Cost Search (UCS), and A* search."
)


# ==================================================
# FLOOR PLAN IMAGE
# ==================================================

st.subheader("🏢 Building Floor Plan")

image_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "images",
    "building_layout.png"
)

if os.path.exists(image_path):
    st.image(
        image_path,
        caption="Building Floor Plan — Rooms 101–112",
        width="stretch"
    )
else:
    st.warning(
        "Floor-plan image not found. Place building_layout.png "
        "inside the images folder."
    )


# ==================================================
# BUILDING GRAPH
# ==================================================

# This is a simplified proposed graph based on the image.
# Verify every connection against the actual building doors.

graph = {
    "Room 101": ["Left Passage"],
    "Room 102": ["Upper Corridor"],
    "Room 103": ["Upper Corridor"],
    "Room 104": ["Upper Corridor"],
    "Room 105": ["Upper Corridor"],
    "Room 106": ["Right Passage"],
    "Room 107": ["Left Passage"],
    "Room 108": ["Right Passage"],
    "Room 109": ["Lower Corridor"],
    "Room 110": ["Lower Corridor"],
    "Room 111": ["Lower Corridor"],
    "Room 112": ["Lower Corridor"],

    "Lobby": [
        "Upper Corridor",
        "Lower Corridor",
        "Left Passage",
        "Right Passage"
    ],

    "Upper Corridor": [
        "Room 102",
        "Room 103",
        "Room 104",
        "Room 105",
        "Lobby",
        "Left Passage",
        "Right Passage",
        "Exit 2",
        "Exit 3"
    ],

    "Lower Corridor": [
        "Room 109",
        "Room 110",
        "Room 111",
        "Room 112",
        "Lobby",
        "Left Passage",
        "Right Passage",
        "Exit 1",
        "Exit 4"
    ],

    "Left Passage": [
        "Room 101",
        "Room 107",
        "Lobby",
        "Upper Corridor",
        "Lower Corridor",
        "Exit 1",
        "Exit 2"
    ],

    "Right Passage": [
        "Room 106",
        "Room 108",
        "Lobby",
        "Upper Corridor",
        "Lower Corridor",
        "Exit 3",
        "Exit 4"
    ],

    "Exit 1": ["Lower Corridor", "Left Passage"],
    "Exit 2": ["Upper Corridor", "Left Passage"],
    "Exit 3": ["Upper Corridor", "Right Passage"],
    "Exit 4": ["Lower Corridor", "Right Passage"]
}


# Ensure every connection works in both directions.
for node, neighbors in list(graph.items()):
    for neighbor in neighbors:
        if neighbor not in graph:
            raise ValueError(f"Unknown building location: {neighbor}")

        if node not in graph[neighbor]:
            graph[neighbor].append(node)


# ==================================================
# PATH COSTS
# ==================================================

# Moving between rooms and their connecting passages
# costs 2. Moving between other locations costs 1.

costs = {}

for node, neighbors in graph.items():
    for neighbor in neighbors:
        if node.startswith("Room ") or neighbor.startswith("Room "):
            costs[(node, neighbor)] = 2
        else:
            costs[(node, neighbor)] = 1


# ==================================================
# MAP POSITIONS
# ==================================================

# Approximate graph layout for route visualization.
# This is not a scale drawing of the actual building.

positions = {
    "Exit 2": (0, 4),
    "Room 102": (1, 4),
    "Room 103": (2, 4),
    "Room 104": (3, 4),
    "Room 105": (4, 4),
    "Exit 3": (5, 4),

    "Upper Corridor": (2.5, 3),

    "Room 101": (0, 1),
    "Room 107": (0, -1),
    "Left Passage": (0.5, 0),

    "Lobby": (2.5, 0),

    "Room 106": (5, 1),
    "Room 108": (5, -1),
    "Right Passage": (4.5, 0),

    "Lower Corridor": (2.5, -2),

    "Exit 1": (0, -4),
    "Room 109": (1, -4),
    "Room 110": (2, -4),
    "Room 111": (3, -4),
    "Room 112": (4, -4),
    "Exit 4": (5, -4)
}


# ==================================================
# DRAW EVACUATION MAP
# ==================================================

def show_building_map(
    building_graph,
    node_positions,
    path=None,
    danger=None,
    blocked_edges=None
):
    path = path or []
    danger = danger or []
    blocked_edges = blocked_edges or set()

    fig, ax = plt.subplots(figsize=(13, 8))

    drawn_edges = set()

    # Draw graph connections.
    for node, neighbors in building_graph.items():
        for neighbor in neighbors:

            edge = tuple(sorted((node, neighbor)))

            if edge in drawn_edges:
                continue

            drawn_edges.add(edge)

            x1, y1 = node_positions[node]
            x2, y2 = node_positions[neighbor]

            if (
                (node, neighbor) in blocked_edges
                or (neighbor, node) in blocked_edges
            ):
                ax.plot(
                    [x1, x2],
                    [y1, y2],
                    color="gray",
                    linestyle="--",
                    linewidth=2,
                    zorder=1
                )

            elif node in danger or neighbor in danger:
                ax.plot(
                    [x1, x2],
                    [y1, y2],
                    color="red",
                    linestyle=":",
                    linewidth=2,
                    zorder=1
                )

            else:
                ax.plot(
                    [x1, x2],
                    [y1, y2],
                    color="lightgray",
                    linewidth=1.8,
                    zorder=1
                )

    # Highlight the selected route.
    for node1, node2 in zip(path, path[1:]):
        x1, y1 = node_positions[node1]
        x2, y2 = node_positions[node2]

        ax.plot(
            [x1, x2],
            [y1, y2],
            color="green",
            linewidth=4,
            solid_capstyle="round",
            zorder=3
        )

    # Draw all locations.
    for node, (x, y) in node_positions.items():

        if node in danger:
            color = "red"
            marker = "X"
            size = 260

        elif node.startswith("Exit"):
            color = "green"
            marker = "s"
            size = 200

        elif node.startswith("Room "):
            color = "lightskyblue"
            marker = "o"
            size = 180

        elif node == "Lobby":
            color = "wheat"
            marker = "D"
            size = 230

        else:
            color = "lightgray"
            marker = "o"
            size = 180

        ax.scatter(
            x,
            y,
            color=color,
            marker=marker,
            s=size,
            edgecolors="black",
            linewidths=0.6,
            zorder=4
        )

        ax.annotate(
            node,
            (x, y),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center",
            fontsize=8,
            fontweight="bold",
            zorder=5
        )

    # Legend.
    ax.plot(
        [], [], color="green", linewidth=4,
        label="Recommended Route"
    )
    ax.plot(
        [], [], color="gray", linestyle="--",
        linewidth=2, label="Blocked Path"
    )
    ax.plot(
        [], [], color="red", linestyle=":",
        linewidth=2, label="Danger-Affected Connection"
    )
    ax.scatter(
        [], [], color="green", marker="s",
        s=100, label="Emergency Exit"
    )
    ax.scatter(
        [], [], color="red", marker="X",
        s=100, label="Danger Zone"
    )

    ax.set_title("Evacuation Route Graph", fontsize=15)
    ax.set_xlabel("Approximate Building Position")
    ax.set_ylabel("Approximate Building Position")
    ax.grid(alpha=0.2)
    ax.set_aspect("equal", adjustable="datalim")
    ax.legend(loc="best", fontsize=8)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ==================================================
# EVACUATION SETTINGS
# ==================================================

st.divider()
st.subheader("📍 Evacuation Settings")

all_locations = list(graph.keys())
exit_locations = ["Exit 1", "Exit 2", "Exit 3", "Exit 4"]

col1, col2 = st.columns(2)

with col1:
    start = st.selectbox(
        "Starting Location",
        all_locations,
        index=all_locations.index("Room 101")
    )

with col2:
    goal = st.selectbox(
        "Emergency Exit",
        exit_locations,
        index=0
    )

algorithm = st.selectbox(
    "Choose Search Algorithm",
    ["BFS", "UCS", "A*"]
)


# ==================================================
# DANGER ZONE
# ==================================================

st.subheader("⚠️ Safety Conditions")

room_locations = [
    f"Room {number}" for number in range(101, 113)
]

danger_options = ["None"] + room_locations

danger_zone = st.selectbox(
    "Select Danger Zone",
    danger_options,
    index=danger_options.index("Room 104")
)

danger_nodes = []

if danger_zone != "None":
    danger_nodes.append(danger_zone)


# ==================================================
# BLOCKED PATH
# ==================================================

st.subheader("🚧 Blocked Path")

all_edges = []

for node, neighbors in graph.items():
    for neighbor in neighbors:
        edge = tuple(sorted((node, neighbor)))
        if edge not in all_edges:
            all_edges.append(edge)

all_edges.sort()

blocked_options = ["None"] + [
    f"{node1} ↔ {node2}"
    for node1, node2 in all_edges
]

blocked_path = st.selectbox(
    "Select Blocked Connection",
    blocked_options
)

blocked_edges = set()

if blocked_path != "None":
    selected_index = blocked_options.index(blocked_path) - 1
    node1, node2 = all_edges[selected_index]

    blocked_edges.add((node1, node2))
    blocked_edges.add((node2, node1))


# ==================================================
# FIND SAFE EVACUATION ROUTE
# ==================================================

st.divider()

if st.button(
    "🚨 Find Safe Evacuation Route",
    width="stretch"
):

    # Reject a destination that is in the danger zone.
    if goal in danger_nodes:
        st.error(
            f"{goal} is marked as dangerous. "
            "Select a different emergency exit."
        )
        st.stop()

    # Copy the graph to preserve the original.
    safe_graph = {
        node: neighbors.copy()
        for node, neighbors in graph.items()
    }

    # Prevent entry into a dangerous room.
    # If the start is in that room, departure is allowed.
    for danger_node in danger_nodes:
        for node in safe_graph:
            if node == danger_node:
                continue

            safe_graph[node] = [
                neighbor
                for neighbor in safe_graph[node]
                if neighbor != danger_node
            ]

    # Remove blocked edges in both directions.
    for node1, node2 in blocked_edges:
        if node2 in safe_graph.get(node1, []):
            safe_graph[node1].remove(node2)

    # Search for a route.
    try:
        if algorithm == "BFS":
            path = bfs(
                safe_graph,
                start,
                goal,
                blocked_edges
            )
            total_cost = None

        elif algorithm == "UCS":
            path, total_cost = ucs(
                safe_graph,
                start,
                goal,
                costs,
                blocked_edges
            )

        else:
            path, total_cost = a_star(
                safe_graph,
                start,
                goal,
                positions,
                costs,
                blocked_edges
            )

        if not path:
            st.error(
                "No safe evacuation route was found. "
                "Try another exit or change the danger zone "
                "or blocked connection."
            )

        else:
            st.success("A route was found in the modeled building graph.")

            st.subheader("🟢 Recommended Evacuation Route")
            st.write(" → ".join(path))

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric("Locations in Route", len(path))

            with metric2:
                if total_cost is not None:
                    st.metric("Total Route Cost", total_cost)
                else:
                    st.metric("Search Algorithm", "BFS")

            st.subheader("🗺️ Evacuation Route Visualization")

            show_building_map(
                graph,
                positions,
                path=path,
                danger=danger_nodes,
                blocked_edges=blocked_edges
            )

            st.subheader("📋 Evacuation Summary")

            st.write(f"**Starting Location:** {start}")
            st.write(f"**Destination:** {goal}")
            st.write(f"**Search Algorithm:** {algorithm}")
            st.write(f"**Route:** {' → '.join(path)}")
            st.write(
                f"**Danger Zone:** "
                f"{', '.join(danger_nodes) if danger_nodes else 'None'}"
            )
            st.write(
                f"**Blocked Path:** "
                f"{blocked_path}"
            )

            if algorithm == "BFS":
                st.caption(
                    "BFS minimizes the number of graph connections, "
                    "not their weighted cost."
                )
            else:
                st.caption(
                    "The route cost is calculated using the configured "
                    "connection costs."
                )

    except Exception as error:
        st.error("An error occurred while calculating the route.")
        st.exception(error)


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Emergency Evacuation Path Finder | "
    "BFS • UCS • A* Search"
)

st.warning(
    "Demonstration only. The graph is a simplified model and has not "
    "been validated against a real building. Do not use this application "
    "for actual emergency navigation without professional validation."
)