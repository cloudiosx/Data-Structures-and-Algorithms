import math

def max_value(nums):
  max = -math.inf # pointer
  for integer in nums:
  	if integer > max:
  		max = integer
  return max
