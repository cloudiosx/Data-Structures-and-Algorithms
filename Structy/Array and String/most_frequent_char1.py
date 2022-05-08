# Time: O(n) | Space: O(n) | n = length of string

def most_frequent_char(s):
	hashmap = {}

	for char in s:
		if char not in hashmap:
			hashmap[char] = 0

		hashmap[char] += 1

	max_key = None

	for char in s:
		if max_key is None or hashmap[char] > hashmap[max_key]:
			max_key = char

	return max_key

