# Input: haystack = "hello", needle = "ll"
# Output: 2

# def strStr(haystack, needle):
# 	if needle == "":
# 		return 0

# 	if needle in haystack:
# 		return haystack.index(needle) # haystack.find(needle)

# 	return -1

def strStr(haystack, needle):
	for i in range(len(haystack) - len(needle) + 1): # for i in 4: 0, 1, 2, 3
		if haystack[i:i + len(needle)] == needle: # "hello"[0:2] == "ll", "hello"[1:3] == "ll", "hello"[2:4] == "ll"
			return i # 2
	return -1

haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))

