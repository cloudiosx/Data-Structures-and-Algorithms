class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(1) | n = # of nodes
# Iterative
def reverse_list(head):
  previous = None
  current = head # current = A
  
  while current is not None: # A, B
    next = current.next # next = B, next = C
    current.next = previous # A --> B = A --> None, B --> C = B --> A
    previous = current # previous = A, previous = B
    current = next # current = B, current = C
    
  return previous

# Time complexity: O(n) | Space complexity: O(n) | n = # of nodes
# Recursive
def reverse_list(head, previous = None):
  if head is None:
    return previous
  next = head.next
  head.next = previous
  return reverse_list(next, head)