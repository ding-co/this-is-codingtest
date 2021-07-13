# BFS (Breadth First Search) example

from collections import deque

# bfs function
def bfs(graph, start_node, visited):
  queue = deque([start_node])
  visited[start_node] = True

  while queue:
    v = queue.popleft()
    print(v, end = " ")

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
    
    print()

# Representation of Graph node connection (Adjacent list way)
# standard: low number prioirty 
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# each node's visited state initialization
visited = [False] * 9

# bfs function call
bfs(graph, 1, visited)