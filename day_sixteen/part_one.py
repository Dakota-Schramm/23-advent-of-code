SPLITTERS = ["|", "-"]
MIRRORS = ["/", "\\"]
EMPTY_SPACE = "."

print(MIRRORS)

class Solution:
  def __init__(self, contraption_layout):
    self.contraption_layout = contraption_layout
    self.print_layout = [list(val) for val in contraption_layout]
    self.m = len(contraption_layout)
    self.n = len(contraption_layout[0])
    light = {
      "direction": "RIGHT",
      "current": (0, 0)
    }
    self.energized = set()
    self.stack = [light]

  def find_light_path(self):
    while len(self.stack):
      val = self.stack.pop()
      self._process_tile(val)

  def find_total_energized(self):
    if len(self.energized) == 0: self.find_light_path()
    self.print_contraption_path()
    return len(self.energized)
  
  def print_contraption_path(self):
    print("Original")
    for line in self.contraption_layout:
      print("".join(line))
    print("Path")
    for line in self.print_layout:
      print("".join(line))

  def _process_tile(self, tile):
    print(tile)
    if not tile or tile["current"] in self.energized: return

    direction = tile["direction"]
    current = tile["current"]
    row, col = current 

    if row < 0 or self.m <= row: return
    if col < 0 or self.n <= col: return

    self.energized.add(current)
    value = self.contraption_layout[ current[0] ][ current[1] ]
    if value == EMPTY_SPACE:
      print(tile, value)
      self.print_layout[row][col] = {
        "LEFT": "<",
        "RIGHT": ">",
        "UP": "^",
        "DOWN": "v",
      }[direction]

      next_space = self._get_next_space(tile)
      print("NEXT =>", next_space)
      self._process_tile(next_space)
    elif value in MIRRORS:            self._determine_mirror_behavior(tile)
    elif value in SPLITTERS:        self._determine_splitter_behavior(tile)
    else:                           raise Exception("Unexpected error occurred")
  
  def _determine_mirror_behavior(self, tile):
    direction = tile["direction"]
    current = tile["current"]
    value = self.contraption_layout[ current[0] ][ current[1] ]
    reflected = { "direction": None, "current": current }

    if value == MIRRORS[0]:
      if direction == "LEFT":
        reflected["direction"] = "DOWN"
        reflected["current"] = self._get_next_space(reflected)["current"]
        self._process_tile(reflected)
      elif direction == "RIGHT":
        reflected["direction"] = "UP"
        reflected["current"] = self._get_next_space(reflected)["current"]
        self._process_tile(reflected)
      elif direction == "UP":
        reflected["direction"] = "RIGHT"
        reflected["current"] = self._get_next_space(reflected)["current"]
        self._process_tile(reflected)
      elif direction == "DOWN":
        reflected["direction"] = "LEFT"
        reflected["current"] = self._get_next_space(reflected)["current"]
        self._process_tile(reflected)
      else: raise Exception("Invalid direction")
    elif value == MIRRORS[1]:
      if direction == "LEFT":
        reflected["direction"] = "UP"
        reflected["current"] = self._get_next_space(reflected)["current"]
        self._process_tile(reflected)
      elif direction == "RIGHT":
        reflected["direction"] = "DOWN"
        reflected["current"] = self._get_next_space(reflected)["current"]
        self._process_tile(reflected)
      elif direction == "UP":
        reflected["direction"] = "LEFT"
        reflected["current"] = self._get_next_space(reflected)["current"]
        self._process_tile(reflected)
      elif direction == "DOWN":
        reflected["direction"] = "RIGHT"
        reflected["current"] = self._get_next_space(reflected)["current"]
        self._process_tile(reflected)
      else: raise Exception("Invalid direction")
    else: raise Exception("Not a mirror")

  def _determine_splitter_behavior(self, tile):
    direction = tile["direction"]
    current = tile["current"]
    value = self.contraption_layout[ current[0] ][ current[1] ]

    if value == SPLITTERS[0]:
      print("HIT", tile)
      if direction in ["UP", "DOWN"]:
        next_space = self._get_next_space(tile)
        self._process_tile(next_space)
      else:
        self._process_tile({
          "direction": "UP",
          "current": (current[0], current[1]-1 )
        })
        self._process_tile({
          "direction": "DOWN",
          "current": (current[0], current[1]+1 )
        })
    elif value == SPLITTERS[1]:
      if direction in ["LEFT", "RIGHT"]:
        next_space = self._get_next_space(tile)
        self._process_tile(next_space)
      else:
        self._process_tile({
          "direction": "LEFT",
          "current": (current[0]-1, current[1])
        })
        self._process_tile({
          "direction": "RIGHT",
          "current": (current[0]+1, current[1])
        })
    else: raise Exception("Not a splitter")

  def _get_next_space(self, tile):
    direction = tile["direction"]
    current = tile["current"]
    row, col = current 

    if row < 0 or self.m <= row: return
    if col < 0 or self.n <= col: return

    next_space = { "direction": direction, "current": None }
    next_space["current"] = {
      "LEFT": (row - 1, col),
      "RIGHT": (row + 1, col),
      "UP": (row, col - 1),
      "DOWN": (row, col + 1),
    }[direction]

    return next_space

if __name__ == "__main__":
  layout = []
  with open("day_sixteen/example_one.txt") as file:
  # with open("day_sixteen.txt") as file:
    for line in file:
      layout.append([ char for char in line.strip() ])
  
  solution = Solution(layout)
  print(solution.find_total_energized())