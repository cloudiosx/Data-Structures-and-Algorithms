class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
# Iterative - Time: O(max(n, m)) | Space: O(max(n, m)) | n = length of list 1, m = length of list 2
    
def add_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  
  carry = 0
  current_1 = head_1
  current_2 = head_2
  while current_1 is not None or current_2 is not None or carry == 1:
    val_1 = 0 if current_1 is None else current_1.val
    val_2 = 0 if current_2 is None else current_2.val
    sum = val_1 + val_2 + carry
    carry = 1 if sum > 9 else 0
    digit = sum % 10
    
    tail.next = Node(digit)
    tail = tail.next
    
    if current_1 is not None:
      current_1 = current_1.next
      
    if current_2 is not None:
      current_2 = current_2.next
      
  return dummy_head.next

# Approach #2

def add_lists(head_1, head_2):
  current_1 = head_1
  current_2 = head_2
  dummy_node = Node(None)
  tail = dummy_node
  previous_sum = 0
  left_with_carry = False
  
  while current_1 is not None and current_2 is not None:
    sum = current_1.val + current_2.val
    if sum > 9:
      if previous_sum > 9:
        ones_digit = sum % 10
        tail.next = Node(ones_digit + 1)
        tail = tail.next
      else:
        ones_digit = sum % 10
        tail.next = Node(ones_digit)
        tail = tail.next
      previous_sum = sum
    else:
      if previous_sum > 9:
        tail.next = Node(sum + 1)
        tail = tail.next
      else:
        tail.next = Node(sum)
        tail = tail.next
      previous_sum = sum
    
    current_1 = current_1.next
    current_2 = current_2.next
  
  if previous_sum > 9:
    left_with_carry = True
  
  carry = 1
  has_carry = True
  
  if not left_with_carry:
    if current_1 is not None:
      tail.next = current_1
    if current_2 is not None:
      tail.next = current_2
  else:
    if current_1 is not None:
      while current_1 is not None:
        if current_1.val == 9:
          sum = current_1.val + carry
          ones_digit = sum % 10
          tail.next = Node(ones_digit)
          tail = tail.next
          has_carry = True
        else:
          tail.next = Node(current_1.val)
          tail = tail.next
          has_carry = False
        current_1 = current_1.next
    if current_2 is not None:
      while current_2 is not None:
        if current_2.val == 9:
          sum = current_2.val + carry
          ones_digit = sum % 10
          tail.next = Node(ones_digit)
          tail = tail.next
          has_carry = True
        else:
          tail.next = Node(current_1.val)
          tail = tail.next
          has_carry = False
        current_2 = current_2.next
             
    if has_carry:
      tail.next = Node(1)
        
  return dummy_node.next

# Recursive - Time: O(max(n, m)) | Space: O(max(n, m)) | n = length of list 1, m = length of list 2

def add_lists(head_1, head_2, carry = 0):
  if head_1 is None and head_2 is None and carry == 0:
    return None
  
  val_1 = 0 if head_1 is None else head_1.val
  val_2 = 0 if head_2 is None else head_2.val  
  sum = val_1 + val_2 + carry
  next_carry = 1 if sum > 9 else 0
  digit = sum % 10
  
  result = Node(digit)
  
  next_1 = None if head_1 is None else head_1.next
  next_2 = None if head_2 is None else head_2.next
  
  result.next = add_lists(next_1, next_2, next_carry)
  return result
