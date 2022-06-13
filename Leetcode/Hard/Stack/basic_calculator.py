# import operator
# def calculate(s):
# 	ops = { "+": operator.add, "-": operator.sub }
# 	numbers = '0123456789'
# 	operations = '+-'
# 	space = ' '
# 	symbols = '()'
# 	stack = [0]
# 	for char in s:
# 		if char == '(':
# 			stack.append(0)
# 		else:
# 			if char == ')':
# 				stack.append(0)
# 			elif char == space:
# 				continue
# 			elif char in numbers:
# 				if len(stack) > 0 and str(stack[-1]) in operations:
# 					operation = stack.pop()
# 					prev_num = stack.pop()
# 					total = ops[operation](int(prev_num), int(char))
# 					stack.append(total)
# 				else:
# 					stack.append(char)
# 			elif char in operations:
# 				stack.append(char)
# 	print(stack)
# 	copy = stack.copy()	
# 	check = False
# 	for ele in stack:
# 		if str(ele) in operations:
# 			check = True

# 	if check:
# 		res = 0
# 		while len(stack) > 0:
# 			item = stack.pop()
# 			if isinstance(item, int):
# 				if len(stack) > 0 and str(stack[-1]) in operations:
# 					operation = stack.pop()
# 					prev_num = stack.pop()
# 					total = ops[operation](int(prev_num), int(item))
# 					res += total
# 				else:
# 					res += item
# 		if copy[1] == '-':
# 			return -abs(res)
# 		else:
# 			return res
# 	else:
# 		total_str = ''
# 		total_int = 0
# 		for ele in stack:
# 			if isinstance(ele, str):
# 				total_str += ele
# 			else:
# 				total_int += ele
		
# 		if total_str == '':
# 			return total_int
# 		else:
# 			return total_str

def calculate(s):
	stack = []
	sum = 0
	sign = 1
	i = 0
	while i < len(s):
		ch = s[i]
		if ch.isdigit():
			res = 0
			while i < len(s) and s[i].isdigit():
				res = res*10+int(s[i])
				i += 1
			i -= 1
			sum += res*sign
			sign = 1
		elif ch == "-":
			sign *= -1
		elif ch == "(":
			stack.append(sum)
			stack.append(sign)
			sum = 0
			sign = 1
		elif ch == ")":
			sum *= stack.pop()
			sum += stack.pop()
		i += 1
	return sum
	# if sum <= (1 << 31):
	# 	return sum
	# return (1 << 31)-1
			
print(calculate('(45-5+2)+3'))
