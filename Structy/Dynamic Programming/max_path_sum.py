def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, row, column, memo):
  pos = (row, column)
  if pos in memo:
    return memo[pos]

  if row == len(grid) or column == len(grid[0]):
    return float('-inf')

  if row == len(grid) - 1 and column == len(grid[0]) - 1:
    return grid[row][column]

  down  = _max_path_sum(grid, row + 1, column, memo)
  right = _max_path_sum(grid, row, column + 1, memo)
  memo[pos] = grid[row][column] + max(down, right)
  return memo[pos]