class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(n) | n = array length
# Iterative
def create_linked_list(values):
  dummy_node = Node('')
  tail = dummy_node
  
  for value in values:
    tail.next = Node(value)
    tail = tail.next

  return dummy_node.next



