from collections import deque
import heapq
import math


# ==================================================
# HELPER FUNCTION
# ==================================================

def is_blocked(node1, node2, blocked_edges):
    """Return True if a connection is explicitly blocked."""
    return (
        (node1, node2) in blocked_edges
        or (node2, node1) in blocked_edges
    )


def edge_cost(costs, node1, node2):
    """Return the configured cost of a connection."""
    cost = costs.get((node1, node2))

    if cost is None:
        cost = costs.get((node2, node1), 1)

    return cost


# ==================================================
# BREADTH-FIRST SEARCH (BFS)
# ==================================================

def bfs(graph, start, goal, blocked_edges=None):
    """
    Find a route with the fewest graph connections.

    Returns:
        A list of locations, or [] if no route exists.
    """

    blocked_edges = blocked_edges or set()

    if start not in graph or goal not in graph:
        return []

    if start == goal:
        return [start]

    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        for neighbor in graph.get(current, []):

            if neighbor in visited:
                continue

            if is_blocked(current, neighbor, blocked_edges):
                continue

            new_path = path + [neighbor]

            if neighbor == goal:
                return new_path

            visited.add(neighbor)
            queue.append(new_path)

    return []


# ==================================================
# UNIFORM COST SEARCH (UCS)
# ==================================================

def ucs(
    graph,
    start,
    goal,
    costs,
    blocked_edges=None
):
    """
    Find a route with the lowest total configured cost.

    Returns:
        (path, total_cost)

        If no route exists, returns ([], float("inf")).
    """

    blocked_edges = blocked_edges or set()

    if start not in graph or goal not in graph:
        return [], float("inf")

    if start == goal:
        return [start], 0

    priority_queue = [(0, start, [start])]
    best_cost = {start: 0}

    while priority_queue:
        current_cost, current, path = heapq.heappop(priority_queue)

        if current_cost > best_cost.get(current, float("inf")):
            continue

        if current == goal:
            return path, current_cost

        for neighbor in graph.get(current, []):

            if neighbor in path:
                continue

            if is_blocked(current, neighbor, blocked_edges):
                continue

            step_cost = edge_cost(costs, current, neighbor)

            if step_cost < 0:
                raise ValueError(
                    "UCS requires non-negative connection costs."
                )

            new_cost = current_cost + step_cost

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost

                heapq.heappush(
                    priority_queue,
                    (
                        new_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return [], float("inf")


# ==================================================
# A* SEARCH
# ==================================================

def heuristic(node, goal, positions):
    """
    Estimate remaining cost using Euclidean distance.

    Scaling the distance by 0.5 keeps the heuristic conservative
    for the approximate coordinates and configured costs used here.
    """

    if node not in positions or goal not in positions:
        return 0

    x1, y1 = positions[node]
    x2, y2 = positions[goal]

    distance = math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2
    )

    return distance * 0.5


def a_star(
    graph,
    start,
    goal,
    positions,
    costs,
    blocked_edges=None
):
    """
    Find a route using A* search.

    Returns:
        (path, total_cost)

        If no route exists, returns ([], float("inf")).
    """

    blocked_edges = blocked_edges or set()

    if start not in graph or goal not in graph:
        return [], float("inf")

    if start == goal:
        return [start], 0

    start_h = heuristic(start, goal, positions)

    priority_queue = [
        (start_h, 0, start, [start])
    ]

    best_cost = {start: 0}

    while priority_queue:
        estimated_total, current_cost, current, path = (
            heapq.heappop(priority_queue)
        )

        if current_cost > best_cost.get(current, float("inf")):
            continue

        if current == goal:
            return path, current_cost

        for neighbor in graph.get(current, []):

            if neighbor in path:
                continue

            if is_blocked(current, neighbor, blocked_edges):
                continue

            step_cost = edge_cost(costs, current, neighbor)

            if step_cost < 0:
                raise ValueError(
                    "A* requires non-negative connection costs."
                )

            new_cost = current_cost + step_cost

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost

                estimate = (
                    new_cost
                    + heuristic(neighbor, goal, positions)
                )

                heapq.heappush(
                    priority_queue,
                    (
                        estimate,
                        new_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return [], float("inf")