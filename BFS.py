from collections import deque
graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    vertex = input("Enter vertex: ")
    neighbours = input(f"Enter neighbours of {vertex} separated by space: ").split()
    graph[vertex] = neighbours
start = input("Enter starting vertex: ")
visited = set()
queue = deque()
visited.add(start)
queue.append(start)
print("BFS Traversal:")
while queue:
    node = queue.popleft()
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
