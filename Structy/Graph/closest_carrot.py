# Time: O(rc) | Space: O(rc) | r = number of rows, c = number of columns

from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set((starting_row, starting_col))
  queue = deque([(starting_row, starting_col, 0)])

  while queue:
    row, col, distance = queue.popleft()

    if grid[row][col] == "C":
      return distance

    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for delta in deltas:
      r_increment, c_increment = delta
      new_row = row + r_increment
      new_col = col + c_increment

      row_in_bounds = 0 <= new_row < len(grid)
      col_in_bounds = 0 <= new_col < len(grid[0])

      position = (new_row, new_col)

      if row_in_bounds and col_in_bounds and grid[new_row][new_col] != "X" and position not in visited:
        queue.append((new_row, new_col, distance + 1))
        visited.add(position)

  return -1
