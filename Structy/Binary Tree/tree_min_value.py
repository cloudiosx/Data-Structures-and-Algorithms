# Time: O(n) | Space: O(n) | n = # of nodes

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# DFT - Iterative
def tree_min_value(root):
  stack = [root]
  smallest = float('inf')

  while stack:
    current = stack.pop()
    if current.val < smallest:
      smallest = current.val

    if current.right is not None:
      stack.append(current.right)

    if current.left is not None:
      stack.append(current.left)

  return smallest

# DFT - Recursive
def tree_min_value(root):
  if root is None:
    return float('inf')

  return min(root.val, tree_min_value(root.left), tree_min_value(root.right))

# BFT - Iterative
from collections import deque
def tree_min_value(root):
  queue = deque([root])
  smallest = float('inf')
  while queue:
    current = queue.popleft()
    if current.val < smallest:
      smallest = current.val

    if current.left is not None:
      queue.append(current.left)

    if current.right is not None:
      queue.append(current.right)
  return smallest