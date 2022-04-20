class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(1) | n = # of nodes
# Iterative
def get_node_value(head, index):
  count = 0
  current = head
  while current is not None:
    if count == index:
      return current.val
    count += 1
    current = current.next
  return None

# Time complexity: O(n) | Space complexity: O(n) | n = # of nodes
# Recursive
def get_node_value(head, index):
  if head is None:
    return None
  if index == 0:
    return head.val
  return get_node_value(head.next, index - 1)