# Time: O(n) | Space: O(n) | n = # of nodes

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Iterative - Time: O(n)
from collections import deque

def tree_sum(root):
  if root is None:
    return 0

  sum = 0
  queue = deque([ root ])

  while queue:
    current = queue.popleft()
    sum += current.val

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)

  return sum

# Recursive
def tree_sum(root):
  if root is None:
    return 0

  left_values = tree_sum(root.left)
  right_values = tree_sum(root.right)

  return root.val + left_values + right_values
