# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
	if len(strs) == 0:
		return ""

	return helper(min(strs), max(strs))

def helper(minString, maxString):
	i = 0
	while i < len(minString) and i < len(maxString) and minString[i] == maxString[i]:
		i += 1
	return minString[:i]

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
