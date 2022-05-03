def addBinary(a, b):
	binary1 = a
	binary2 = b
	integer_sum = int(binary1, 2) + int(binary2, 2)
	binary_sum = bin(integer_sum)
	return binary_sum[2:]

# a = "11"
# b = "1"

a = "1010"
b = "1011"
print(addBinary(a, b))
