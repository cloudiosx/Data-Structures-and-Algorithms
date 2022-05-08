# Time: O(n) | Space: O(n) | n = length of numbers list

def pair_product(numbers, target_product):
	hashmap = {}

	for idx, number in enumerate(numbers):
		complement = target_product / number

		if complement in hashmap:
			return (idx, hashmap[complement])

		hashmap[number] = idx