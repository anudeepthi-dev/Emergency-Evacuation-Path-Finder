import streamlit as st
import matplotlib.pyplot as plt

from algorithms import bfs, ucs, a_star


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Emergency Evacuation Path Finder",
    page_icon="🚨",
    layout="centered"
)


# ---------------- TITLE ----------------

st.title("🚨 Emergency Evacuation Path Finder")

st.write(
    "Find a safe evacuation route using AI search algorithms."
)


# ---------------- BUILDING GRAPH ----------------

graph = {
    "Entrance": ["Hall"],
    "Hall": ["Entrance", "Room A", "Room B", "Corridor"],
    "Room A": ["Hall", "Exit 1"],
    "Room B": ["Hall", "Exit 2"],
    "Corridor": ["Hall", "Exit 1"],
    "Exit 1": ["Room A", "Corridor"],
    "Exit 2": ["Room B"]
}


# ---------------- PATH COSTS ----------------

costs = {
    ("Entrance", "Hall"): 1,
    ("Hall", "Entrance"): 1,

    ("Hall", "Room A"): 2,
    ("Room A", "Hall"): 2,

    ("Hall", "Room B"): 2,
    ("Room B", "Hall"): 2,

    ("Hall", "Corridor"): 1,
    ("Corridor", "Hall"): 1,

    ("Room A", "Exit 1"): 1,
    ("Exit 1", "Room A"): 1,

    ("Room B", "Exit 2"): 1,
    ("Exit 2", "Room B"): 1,

    ("Corridor", "Exit 1"): 1,
    ("Exit 1", "Corridor"): 1
}


# ---------------- A* COORDINATES ----------------

coordinates = {
    "Entrance": (0, 0),
    "Hall": (1, 0),
    "Room A": (2, 1),
    "Room B": (2, -1),
    "Corridor": (2, 0),
    "Exit 1": (3, 1),
    "Exit 2": (3, -1)
}


# ---------------- LOCATIONS ----------------

locations = list(graph.keys())

danger_options = [
    "None",
    "Room A",
    "Room B",
    "Corridor",
    "Hall"
]

blocked_options = [
    "None",
    "Hall → Room A",
    "Hall → Room B",
    "Hall → Corridor",
    "Room A → Exit 1",
    "Room B → Exit 2",
    "Corridor → Exit 1"
]


# ---------------- BUILDING MAP ----------------

def show_building_map(path=None, blocked_path=None, danger_zone=None):

    positions = {
        "Entrance": (0, 0),
        "Hall": (1, 0),
        "Room A": (2, 1),
        "Room B": (2, -1),
        "Corridor": (2, 0),
        "Exit 1": (3, 1),
        "Exit 2": (3, -1)
    }

    connections = [
        ("Entrance", "Hall"),
        ("Hall", "Room A"),
        ("Hall", "Room B"),
        ("Hall", "Corridor"),
        ("Room A", "Exit 1"),
        ("Room B", "Exit 2"),
        ("Corridor", "Exit 1")
    ]

    fig, ax = plt.subplots(figsize=(9, 5))

    # Draw building connections
    for node1, node2 in connections:

        x1, y1 = positions[node1]
        x2, y2 = positions[node2]

        ax.plot(
            [x1, x2],
            [y1, y2],
            linewidth=2
        )

    # Highlight selected route
    if path:

        for i in range(len(path) - 1):

            x1, y1 = positions[path[i]]
            x2, y2 = positions[path[i + 1]]

            ax.plot(
                [x1, x2],
                [y1, y2],
                linewidth=5
            )

    # Draw locations
    for node, (x, y) in positions.items():

        ax.scatter(
            x,
            y,
            s=900,
            zorder=3
        )

        ax.text(
            x,
            y,
            node,
            ha="center",
            va="center",
            fontsize=9
        )

    # Mark danger zone
    if danger_zone and danger_zone != "None":

        x, y = positions[danger_zone]

        ax.scatter(
            x,
            y,
            s=1100,
            marker="x",
            linewidths=3,
            zorder=4
        )

    # Mark blocked path
    if blocked_path and blocked_path != "None":

        parts = blocked_path.split(" → ")

        node1 = parts[0]
        node2 = parts[1]

        x1, y1 = positions[node1]
        x2, y2 = positions[node2]

        ax.plot(
            [x1, x2],
            [y1, y2],
            linestyle="--",
            linewidth=4
        )

    ax.set_title("Emergency Building Map")

    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-1.7, 1.7)

    ax.axis("off")

    st.pyplot(fig)


# ---------------- USER INPUT ----------------

st.subheader("🚨 Select Evacuation Details")

start = st.selectbox(
    "Starting Location",
    locations
)

goal = st.selectbox(
    "Emergency Exit",
    ["Exit 1", "Exit 2"]
)

algorithm = st.selectbox(
    "Select AI Algorithm",
    ["A*", "BFS", "UCS"]
)

danger_zone = st.selectbox(
    "⚠️ Select Danger Zone",
    danger_options
)

blocked_path = st.selectbox(
    "🚧 Select Blocked Path",
    blocked_options
)


# ---------------- FIND SAFE PATH ----------------

if st.button("🚨 Find Safe Path"):

    # Set of blocked edges
    blocked = set()


    # ---------- BLOCKED PATH ----------

    if blocked_path != "None":

        parts = blocked_path.split(" → ")

        node1 = parts[0]
        node2 = parts[1]

        blocked.add((node1, node2))
        blocked.add((node2, node1))


    # ---------- DANGER ZONE ----------

    if danger_zone != "None":

        for neighbor in graph.get(danger_zone, []):

            blocked.add((danger_zone, neighbor))
            blocked.add((neighbor, danger_zone))


    # If starting location itself is a danger zone,
    # allow the person to leave it.

    if start == danger_zone:

        for neighbor in graph.get(start, []):

            blocked.discard((start, neighbor))
            blocked.discard((neighbor, start))


    # ---------------- RUN ALGORITHM ----------------

    if algorithm == "BFS":

        path = bfs(
            graph,
            start,
            goal,
            blocked
        )

        if path:

            cost = sum(
                costs.get(
                    (path[i], path[i + 1]),
                    1
                )
                for i in range(len(path) - 1)
            )

        else:

            cost = None


    elif algorithm == "UCS":

        path, cost = ucs(
            graph,
            start,
            goal,
            costs,
            blocked
        )

        if path is None:

            cost = None


    else:

        path, cost = a_star(
            graph,
            start,
            goal,
            costs,
            blocked,
            coordinates
        )

        if path is None:

            cost = None


    # ---------------- BUILDING MAP ----------------

    st.subheader("🗺️ Building Map")

    show_building_map(
        path,
        blocked_path,
        danger_zone
    )


    # ---------------- RESULT ----------------

    st.subheader("🛣️ Evacuation Result")


    if path:

        st.success(
            "✅ Safe evacuation route found!"
        )

        if danger_zone != "None":

            st.warning(
                f"⚠️ Danger zone avoided: {danger_zone}"
            )

        if blocked_path != "None":

            st.warning(
                f"🚧 Blocked path avoided: {blocked_path}"
            )

        st.write(
            "### Recommended Safe Route"
        )

        st.info(
            " → ".join(path)
        )

        st.write(
            f"**Total Path Cost:** {cost}"
        )

        st.write(
            f"**Number of Locations:** {len(path)}"
        )


    else:

        st.error(
            "❌ No safe evacuation route is available."
        )

        st.write(
            "Try selecting another emergency exit "
            "or changing the blocked path/danger zone."
        )