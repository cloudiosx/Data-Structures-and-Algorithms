# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def generate(numRows): # 3
	result = [] # [[1], [1, 1]]

	for row_num in range(numRows): # 0, 1, 2
		row = [None for _ in range(row_num + 1)] # [None], [None, None], [None, None, None]

		row[0], row[-1] = 1, 1 # [1], [1, 1], [1, None, 1]

		for j in range(1, row_num): # j = 1, range(1, 2)
			row[j] = result[row_num - 1][j - 1] + result[row_num - 1][j] # [1], [1, 1], [1, 2, 1]

		result.append(row)

	return result # [[1], [1, 1], [1, 2, 1]]
	
numRows = 3
print(generate(numRows))