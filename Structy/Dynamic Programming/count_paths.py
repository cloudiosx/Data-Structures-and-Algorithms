def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, row, column, memo):
  pos = (row, column)

  if pos in memo:
    return memo[pos]

  if row == len(grid) or column == len(grid[0]) or grid[row][column] == 'X':
    return 0

  if row == len(grid) - 1 and column == len(grid[0]) - 1:
    return 1

  down = _count_paths(grid, row + 1, column, memo)
  right = _count_paths(grid, row, column + 1, memo)
  memo[pos] = down + right
  return memo[pos]
