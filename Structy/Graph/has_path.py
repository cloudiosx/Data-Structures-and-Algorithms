# Time: O(e) or O(n^2) | Space: O(n) | e = # of edges, n = # of nodes, n^2 = # of edges

# DFT - Iterative
def has_path(graph, src, dst):
  stack = [src]

  while len(stack) > 0:
    current = stack.pop()
    if current == dst:
      return True

    for neighbor in graph[current]:
      stack.append(neighbor)

  return False

# DFT - Recursive
def has_path(graph, src, dst):
  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True

  return False

# BFT - Iterative
from collections import deque
def has_path(graph, src, dst):
  queue = deque([src])

  while len(queue) > 0:
    current = queue.popleft()
    if current == dst:
      return True

    for neighbor in graph[current]:
      queue.append(neighbor)

  return False