class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def longest_streak(head):
  prev = None
  count = 1
  arr = []
  _longest_streak(head, prev, count, arr)
  print(arr)
  return max(arr)

def _longest_streak(head, prev, count, arr):
  if head is None:
    arr.append(count)
    return None
  
  if prev is not None and prev.val == head.val:
    count += 1
  
  if prev is not None and prev.val != head.val:
    arr.append(count)
    count = 1
  
  _longest_streak(head.next, head, count, arr)

a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

print(longest_streak(a)) # 3