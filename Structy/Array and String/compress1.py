# Time: O(n) | Space: O(n) | n = length of string

def compress(s):
	s += '!'
	i = 0
	j = 0

	result = []

	while j < len(s):
		if s[i] == s[j]:
			j += 1
		else:
			count = j - i
			result.append(s[i]) if count == 1 else result.append(f'{count}{s[i]}')
			i = j

	# # last iteration
	# count = j - i
	# result.append(s[i]) if count == 1 else result.append(f'{count}{s[i]}')
	return "".join(result)

print(compress('ccaaatsss'))