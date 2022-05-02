# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

'''
def dominantIndex(nums):
	if len(nums) == 1:
		return 0       
	n = nums[0:]
	n.sort()
	if n[-1] >= 2 * n[-2]:
		return nums.index(n[-1])    
	return -1
'''

def dominantIndex(nums):
	maximum_number = max(nums)
	check = True
	for i in range(len(nums)):
		if maximum_number < 2 * nums[i] and nums[i] != maximum_number:
			check = False

	if check:
		return nums.index(maximum_number)

	return -1


nums = [3, 6, 1, 0]
print(dominantIndex(nums))

