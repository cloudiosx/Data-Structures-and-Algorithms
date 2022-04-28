# Time: O(rc) | Space: O(rc) | r = number of rows, c = number of columns

def island_count(grid):
  visited = set()
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore(grid, r, c, visited) == True:
        count += 1
  return count

def explore(grid, row, column, visited):
  row_inbounds = 0 <= row < len(grid)
  column_inbounds = 0 <= column < len(grid[0])

  if not row_inbounds or not column_inbounds:
    return False

  if grid[row][column] == "W":
    return False

  position = (row, column)

  if position in visited:
    return False

  visited.add(position)

  explore(grid, row - 1, column, visited)
  explore(grid, row + 1, column, visited)
  explore(grid, row, column - 1, visited)
  explore(grid, row, column + 1, visited)

  return True
