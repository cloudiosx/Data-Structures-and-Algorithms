class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(1) | n = # of nodes
# Iterative
def is_univalue_list(head):
  current = head
  
  while current is not None:
    if current.val != head.val:
      return False
    current = current.next

  return True

# Time complexity: O(n) | Space complexity: O(n) | n = # of nodes
# Recursive
def is_univalue_list(head, prev_val = None):
  if head is None:
    return True

  if prev_val is not None and prev_val != head.val:
    return False

  return is_univalue_list(head.next, head.val)
