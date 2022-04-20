class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(1) | n = # of nodes
# Iterative
def sum_list(head):
  total_sum = 0
  
  current = head
  while current is not None:
    total_sum += current.val
    current = current.next

  return total_sum

# Time complexity: O(n) | Space complexity: O(n) | n = # of nodes
# Recursive
def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)