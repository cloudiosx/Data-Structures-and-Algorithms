class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

# Iterative - Time: O(n) | Space: O(1) | n = number of nodes

def reverse_list(head):
	prev = None
	current = head

	while current is not None:

		next = current.next # Store original current.next here
		current.next = prev
		prev = current
		current = next

	return prev

# Recursive - Time: O(n) | Space: O(n) | n = number of nodes

def reverse_list(head, prev = None):
	if head is None:
		return prev

	next = head.next
	head.next = prev

	return reverse_list(next, head)