# DFS (Depth First Search) example

def dfs(graph, start_node, visited):

  # Handle current node visit
  visited[start_node] = True
  print(start_node, end=' ')

  # Recursive visit other node which is connected to current node
  for i in graph[start_node]:
    if not visited[i]:
      dfs(graph, i, visited)

# Representation of each node's connection (2 Dimension list)
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

# Represent each node's visiting information (1 dimension list)
visited = [False] * 9

# Call defined DFS function
dfs(graph, 1, visited)
print()