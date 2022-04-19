# Time complexity: O(n + m) | Space complexity: O(n)
def intersection(a, b):
	intersection = []
	my_set = set()

	for integer in a:
		my_set.add(integer)

	for integer in b:
		if integer in my_set:
			intersection.append(integer)

	return intersection
