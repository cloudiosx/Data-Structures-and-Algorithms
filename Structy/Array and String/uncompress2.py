# Time: O(n * m) | Space: O(n * m) | n = number of groups, m = max num found in any group

def uncompress(s):
	num = "012345679"
	res = []

	i = 0
	j = 0

	while j < len(s):
		if s[j] in num:
			j += 1
		else:
			res.append(s[j] * int(s[i:j]))
			j += 1
			i = j
		

	return "".join(res)
