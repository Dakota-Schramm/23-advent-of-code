from collections import deque

ROCK = "#"
GARDEN_PLOT = "."

class Solution:
  def __init__(self, grid, s):
    self.grid = grid
    self.s = s
    self.m = len(grid)
    self.n = len(grid[0])
    self.q = deque()
    self.garden_plots = set()
  
  def find_reachable_garden_plots(self):
    self._move_spaces(self.s)
    return len(self.garden_plots)

  def _move_spaces(self, pos, steps_left=64):
    print(pos, steps_left)
    if steps_left < 0: return

    row, col = pos
    if row <= 0 or self.m <= row: return
    if col <= 0 or self.n <= col: return

    val = self.grid[row][col]
    if val == ROCK: return
    if steps_left == 0 and val == GARDEN_PLOT:
      self.garden_plots.add(pos)
      return

    self._move_spaces((row-1, col), steps_left-1)
    self._move_spaces((row+1, col), steps_left-1)
    self._move_spaces((row, col-1), steps_left-1)
    self._move_spaces((row, col+1), steps_left-1)

if __name__ == "__main__":
  grid = []
  s = None
  with open("day_twenty_one/example_one.txt") as file:
  # with open("day_twenty_one.txt") as file:
    for i, line in enumerate(file):
      row = []
      for j, val in enumerate(line.strip()):
        row.append(val)
        if val == "S": s = (i, j)
      grid.append(row)
  
  solution = Solution(grid, s)
  total = solution.find_reachable_garden_plots()
  print(total)
  