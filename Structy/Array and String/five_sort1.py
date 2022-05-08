# Time: O(n) | Space: O(1) | n = array size

def five_sort(nums):
	i = 0
	j = len(nums) - 1

	while i < j:
		if nums[j] == 5:
			j -= 1

		if nums[i] == 5 and nums[j] != 5:
			nums[i] = nums[j]
			nums[j] = 5
			j -= 1
			i += 1

		if nums[i] != 5:
			i += 1

	return nums

def five_sort(nums):
	i = 0
	j = len(nums) - 1

	while i < j:
		if nums[j] == 5:
			j -= 1
		elif nums[i] == 5:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
		else:
			i += 1

	return nums