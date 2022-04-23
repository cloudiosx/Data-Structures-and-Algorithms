# Hashmap | Time: O(n) | Space: O(n) | n = length of the input array
def twoSum(nums, target):
	hashmap = {}

	for idx, num in enumerate(nums):
		complement = target - num
		if complement in hashmap:
			return [idx, hashmap[complement]]

		hashmap[num] = idx
	return

	'''
	hashmap = {}

	for i in range(len(nums)):
		complement = target - nums[i]
		if complement in hashmap:
			return [i, hashmap[complement]]
		hashmap[nums[i]] = i
	return
	'''