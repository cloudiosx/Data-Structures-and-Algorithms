# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

'''
def pivotIndex(nums):
	for i in range(len(nums)):
		left_sum = sum(nums[:i])
		right_sum = sum(nums[i+1:])
		if left_sum == right_sum:
			return i
	return -1
'''

def pivotIndex(nums):
	total_sum = sum(nums)
	for i in range(len(nums)):
		currentNum = nums[i]
		left_sum = sum(nums[:i])
		remaining_sum = total_sum - left_sum
		right_sum = remaining_sum - currentNum
		if left_sum == right_sum:
			return i
	return -1

nums = [1,7,3,6,5,6] 
print(pivotIndex(nums))