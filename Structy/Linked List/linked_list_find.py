class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(1) | n = # of nodes
# Iterative
def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False

# Time complexity: O(n) | Space complexity: O(n) | n = # of nodes
# Recursive
def linked_list_find(head, target):
  if head is None:
    return False
  elif head.val == target:
    return True

  return linked_list_find(head.next, target)