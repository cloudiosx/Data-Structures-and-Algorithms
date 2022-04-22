class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(n) | n = length of values
# Iterative
def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head
  for val in values:
    tail.next = Node(val)
    tail = tail.next
  return dummy_head.next

# Time complexity: O(n^2) | Space complexity: O(n) | n = length of values
# Recursive
def create_linked_list(values):
  if len(values) == 0:
    return None
  head = Node(values[0])
  head.next = create_linked_list(values[1:]) # slice creates new copy in Python
  return head

# Time complexity: O(n) | Space complexity: O(n) | n = length of values
# Recursive
def create_linked_list(values, i = 0):
  if i == len(values):
    return None
  head = Node(values[i])
  head.next = create_linked_list(values, i + 1)
  return head
