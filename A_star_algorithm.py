import heapq

# A* algorithm
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 2), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': [],
}

# HEURISTIC VALUES
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0,
}

def astar(start, goal):

    open_list = [(heuristic[start], start)]


    came_from = {}


    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0


    while open_list:

        current_f_score, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = [goal]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph[current_node]:

            tentative_g_score = g_score[current_node] + cost

            if tentative_g_score < g_score[neighbor]:

                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score

                heapq.heappush(open_list, (tentative_g_score + heuristic[neighbor], neighbor))

    return None, float('inf')

# main program
start_node = input("Enter the start node: ").upper()
goal_node = input("Enter the goal node: ").upper()

# Check if nodes exist in the graph
if start_node not in graph or goal_node not in graph:
    print("Invalid start or goal node. Please enter nodes from A, B, C, D, E, F, G.")
else:
    path, cost = astar(start_node, goal_node)

    if path:
        print("Shortest path:", " --> ".join(path))
        print("Total cost:", cost)
    else:
        print("Path not found.")