# Time: O(n) | Space: O(n) | n = length of numbers list

def pair_sum(numbers, target_sum):
	hashmap = {}
	for idx, number in enumerate(numbers):
		complement = target_sum - number

		if complement in hashmap:
			return (idx, hashmap[complement])

		hashmap[number] = idx