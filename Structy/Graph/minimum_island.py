# Time: O(rc) | Space: O(rc) | r = number of rows, c = number of columns

def minimum_island(grid):
  visited = set()
  minimum = float("inf")
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      size = explore_grid(grid, row, column, visited)
      if size > 0 and size < minimum:
        minimum = size
  return minimum

def explore_grid(grid, row, column, visited):
  row_inbounds = 0 <= row < len(grid)
  col_inbounds = 0 <= column < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return 0

  if grid[row][column] == "W":
    return 0

  position = (row, column)

  if position in visited:
    return 0

  visited.add(position)

  size = 1

  size += explore_grid(grid, row - 1, column, visited)
  size += explore_grid(grid, row + 1, column, visited)
  size += explore_grid(grid, row, column - 1, visited)
  size += explore_grid(grid, row, column + 1, visited)

  return size
