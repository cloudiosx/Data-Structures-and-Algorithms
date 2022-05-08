# Time: O(n) | Space: O(n) | n = length of string

def compress(s):
	s += "!"

	i = 0
	j = 0

	res = []

	while j < len(s):
		if s[j] == s[i]:
			j += 1
		else:
			count = j - i
			res.append(f'{s[i]}') if count == 1 else res.append(f'{count}{s[i]}')
			i = j

	return "".join(res)
