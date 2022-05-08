# Time: O(n + m) | Space: O(n) | n = length of array a, m = length of array b

def intersection(a, b):
	res = []

	hash_set = set()

	for number in a:
		if number in hash_set:
			res.append(number)
		else:
			hash_set.add(number)

	for number in b:
		if number in hash_set:
			res.append(number)
		else:
			hash_set.add(number)

	return res

def intersection(a, b):
	set_a = set(a)
	return [number for number in b if number in set_a]

# Time: O(n * m) | Space: O(min(n, m)) | n = length of array a, m = length of array b

def intersection(a, b):
	return [number for number in a if number in b]