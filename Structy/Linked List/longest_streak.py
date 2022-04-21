class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time complexity: O(n) | Space complexity: O(1) | n = # of nodes
# Iterative
def longest_streak(head):
  max_streak = 0
  current_streak = 0
  prev_val = None
  
  current_node = head
  while current_node is not None:
    if current_node.val == prev_val:
      current_streak += 1
    else:
      current_streak = 1
  
    prev_val = current_node.val
    if current_streak > max_streak:
      max_streak = current_streak
    
    current_node = current_node.next
    
  return max_streak
