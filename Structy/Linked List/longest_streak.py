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
  current = head

  while current is not None:
    if prev_val is None:
      current_streak += 1

    if prev_val is not None and prev_val == current.val:
      current_streak += 1
    elif prev_val != current.val:
      current_streak = 1

    if current_streak > max_streak:
      max_streak = current_streak

    prev_val = current.val
    current = current.next

  return max_streak
