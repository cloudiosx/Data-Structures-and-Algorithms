import math

def max_value(nums):
  max = -math.inf # pointer
  for integer in nums:
  	if integer > max:
  		max = integer
  return max

# Solution

def max_value(nums):
	maximum = float('-inf')

	for num in nums:
		if num > maximum:
			maximum = num

	return maximum

