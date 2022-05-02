def plusOne(digits):
	if digits[-1] == 9:
		if len(digits) == 1: # Already a 9
			return [1, 0]
		return plusOne(digits[:-1]) + [0]
	else:
		digits[-1] += 1
	return digits

digits = [5, 4, 9, 9]
print(plusOne(digits))