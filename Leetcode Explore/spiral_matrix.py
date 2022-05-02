# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(matrix):
	res = []
	helper(matrix, 0, 0, res)
	return res

def helper(matrix, row_index, col_index, res):
	if row_index < 0 or row_index >= len(matrix) or col_index < 0 or col_index >= len(matrix[0]) or matrix[row_index][col_index] == "#":
		return

	res.append(matrix[row_index][col_index])
	matrix[row_index][col_index] = "#"

	if col_index + 1 >= row_index:
		helper(matrix, row_index, col_index + 1, res)
	helper(matrix, row_index + 1, col_index, res)
	helper(matrix, row_index, col_index - 1, res)
	helper(matrix, row_index - 1, col_index, res)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix)) # [1,2,3,6,9,8,7,4,5]

