class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

# Iterative - Time: O(n) | Space: O(n) | n = number of nodes

def linked_list_values(head):
	res = []
	current = head

	while current is not None:
		res.append(current.val)
		current = current.next

	return res

# Recursive - Time: O(n) | Space: O(n) | n = number of nodes

def linked_list_values(head):
	res = []
	_linked_list_values(head, res)
	return res

def _linked_list_values(head, res):
	if head is None:
		return

	res.append(head.val)

	_linked_list_values(head.next, res)