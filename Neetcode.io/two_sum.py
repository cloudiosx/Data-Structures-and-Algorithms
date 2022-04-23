# Hashmap | Time: O(n) | Space: O(n) | n = length of the input array
def twoSum(nums, target):
	hashmap = {}

	for idx, num in enumerate(nums):
		complement = target - num
		if complement in hashmap:
			return [idx, hashmap[complement]]

		hashmap[num] = idx
