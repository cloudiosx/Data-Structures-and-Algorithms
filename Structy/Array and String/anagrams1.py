# Time: O(n + m) | Space: O(n + m) | n = length of string 1, m = length of string 2

def anagrams(s1, s2):
	hashmap_s1 = {}
	hashmap_s2 = {}

	for char in s1:
		if char not in hashmap_s1:
			hashmap_s1[char] = 0

		hashmap_s1[char] += 1

	for char in s2:
		if char not in hashmap_s2:
			hashmap_s2[char] = 0

		hashmap_s2[char] += 1

	if hashmap_s1 == hashmap_s2:
		return True

	return False