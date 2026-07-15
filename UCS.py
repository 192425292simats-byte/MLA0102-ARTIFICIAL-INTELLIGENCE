from queue import PriorityQueue
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}
def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = {}
    while not pq.empty():
        cost, node, path = pq.get()
        if node == goal:
            return path, cost
        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbour, weight in graph[node]:
                pq.put((cost + weight, neighbour, path + [neighbour]))
    return None, float('inf')
start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")
path, cost = uniform_cost_search(graph, start, goal)
if path:
    print("\nShortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Path not found.")
