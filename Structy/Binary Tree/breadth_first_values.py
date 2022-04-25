# Queue | Time: O(n) | Space: O(n) | n = # of nodes

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Iterative - Time: O(n^2)
def breadth_first_values(root):
  if root is None:
    return []

  values = []
  queue = [ root ]

  while queue:
    current = queue.pop(0)
    values.append(current.val)

    if current.left is not None:
      queue.append(current.left)

    if current.right is not None:
      queue.append(current.right)

  return values

from collections import deque

# Iterative - Time: O(n)
def breadth_first_values(root):
  if root is None:
    return []

  values = []
  queue = deque([ root ])

  while queue:
    current = queue.popleft()
    values.append(current.val)

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)

  return values