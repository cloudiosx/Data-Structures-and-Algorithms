# Time: O(n) | Space: O(n) | n = # of nodes

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# BFT - Iterative
from collections import deque
def bottom_right_value(root):
  queue = deque([root])

  current = None
  while queue:
    current = queue.popleft()

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)

  return current.val
