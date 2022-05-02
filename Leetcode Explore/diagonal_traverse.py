# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

from collections import defaultdict

def findDiagonalOrder(mat):
	rows, cols = len(mat), len(mat[0])

	matrix_dict = defaultdict(list)

	for row_index in range(rows):
		for col_index in range(cols):
			matrix_dict[row_index + col_index].append(mat[row_index][col_index])

	result = []

	for idx, val in enumerate(matrix_dict.values()):
		if idx % 2 == 0:
			result.extend(reversed(matrix_dict[idx]))
		else:
			result.extend(matrix_dict[idx])

	return result

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(mat))