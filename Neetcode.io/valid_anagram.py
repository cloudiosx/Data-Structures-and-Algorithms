# Time: O(S + T) | Space: O(S + T) | S = length of s string, T = length of t string
# Hashmap approach
def isAnagram(s, t):
	if len(s) != len(t):
		return False

	countS, countT = {}, {}

	for i in range(len(s)):
		countS[s[i]] = 1 + countS.get(s[i], 0)
		countT[t[i]] = 1 + countT.get(t[i], 0)

	for key in countS:
		if countS[key] != countT.get(key, 0):
			return False

	return True

# Counter approach
from collections import Counter
def isAnagram(s, t):
	return Counter(s) == Counter(t)

# Time: O(nlogn) - O(n^2) | Space: O(1) - O(n) | n = length of the string
def isAnagram(s, t):
	return sorted(s) == sorted(t)