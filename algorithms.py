from collections import deque
import heapq


# ---------------- BFS ----------------
def bfs(graph, start, goal, blocked):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited and (current, neighbor) not in blocked:
                queue.append((neighbor, path + [neighbor]))

    return None


# ---------------- UCS ----------------
def ucs(graph, start, goal, costs, blocked):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, cost

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor in visited:
                continue

            if (current, neighbor) in blocked:
                continue

            new_cost = cost + costs.get((current, neighbor), 1)

            heapq.heappush(
                priority_queue,
                (new_cost, neighbor, path + [neighbor])
            )

    return None, float("inf")


# ---------------- A* ----------------
def heuristic(node, goal, coordinates):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]

    return abs(x1 - x2) + abs(y1 - y2)


def a_star(graph, start, goal, costs, blocked, coordinates):
    priority_queue = [
        (0, start, [start], 0)
    ]

    visited = set()

    while priority_queue:
        f, current, path, g = heapq.heappop(priority_queue)

        if current == goal:
            return path, g

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph.get(current, []):

            if neighbor in visited:
                continue

            if (current, neighbor) in blocked:
                continue

            new_g = g + costs.get((current, neighbor), 1)

            h = heuristic(neighbor, goal, coordinates)

            new_f = new_g + h

            heapq.heappush(
                priority_queue,
                (new_f, neighbor, path + [neighbor], new_g)
            )

    return None, float("inf")