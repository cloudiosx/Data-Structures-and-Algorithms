# Time: O(n) | Space: O(n) | n = # of nodes

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# DFT - Recursive
def how_high(node):
  if node is None:
    return -1

  left_subtree = how_high(node.left)
  right_subtree = how_high(node.right)
  return 1 + max(left_subtree, right_subtree)