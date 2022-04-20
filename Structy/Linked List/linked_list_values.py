class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(n) | n = # of nodes
# Iterative
def linked_list_values(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values

# Time complexity: O(n) | Space complexity: O(n) | n = # of nodes
# Recursive
def linked_list_values(head):
  values = []
  fill_values(head, values)
  return values

def fill_values(head, values):
  if head is None:
    return
  values.append(head.val)
  fill_values(head.next, values)