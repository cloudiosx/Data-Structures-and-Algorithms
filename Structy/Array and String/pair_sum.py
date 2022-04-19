# Time complexity: O(n) | Space complexity: O(n)
def pair_sum(numbers, target_sum):
  previous_nums = {}
  
  for index, num in enumerate(numbers):
    complement = target_sum - num
    
    if complement in previous_nums:
      return (previous_nums[complement], index)
    
    previous_nums[num] = index