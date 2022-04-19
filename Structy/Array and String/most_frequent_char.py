# Time complexity: O(n) | Space complexity: O(n)

# Approach 1
def most_frequent_char(s):
	count = {}
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1
  
  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best

# Approach 2
from collections import Counter

def most_frequent_char(s):
  count = Counter(s)
  
  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best