def uncompress(s):
	# Alphabet
	# alphabet = "abcdefghijklmnopqrstuvwxyz"
	numbers = "012345679"

	# 2 Pointers
	i = 0
	j = 0

	finalArr = []

	while j < len(s):
		if s[j] in numbers:
			j += 1
		else:
			number = int(s[i:j])
			finalArr.append(s[j] * number)
			j += 1
			i = j

	return "".join(finalArr)

print(uncompress("3n12e2z"))


