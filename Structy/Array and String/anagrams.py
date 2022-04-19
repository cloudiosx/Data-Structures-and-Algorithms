# Time complexity: O(n + m) | Space complexity: ~O(n + m)
def anagrams(s1, s2):
	return char_count(s1) == char_count(s2)

def char_count(s):
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    
    count[char] += 1
  
  return count
                      
# Importing Counter structure from Collections built-in module
from collections import Counter

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)

