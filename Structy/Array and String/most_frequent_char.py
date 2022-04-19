# Time complexity: O(n) | Space complexity: O(n)
def most_frequent_char(s):
	maximum = s[0]
	hashmap = {}

	for char in s:
		if char not in hashmap:
			hashmap[char] = 0

		hashmap[char] += 1

	for char in s:
		if hashmap[char] > hashmap[maximum]:
			maximum = char

	return maximum