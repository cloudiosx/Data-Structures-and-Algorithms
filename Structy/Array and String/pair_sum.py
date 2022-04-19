# Time complexity: O(n) | Space complexity: O(n)
def pair_sum(numbers, target_sum):
  previous_nums = {}
  
  for index, num in enumerate(numbers):
    complement = target_sum - num
    
    if complement in previous_nums:
      return (previous_nums[complement], index)
    
    previous_nums[num] = index


# Time complexity: O(n^2) | Space complexity: O(1)
def pair_sum(numbers, target_sum):
	for i in range(0, len(numbers)):
		for j in range(i + 1, len(numbers)):
			if numbers[i] + numbers[j] == target_sum:
				return (i, j)