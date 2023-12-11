def print_node(sketch, pos):
  row, col = pos
  m = len(sketch)
  n = len(sketch[0])
  r_start = r_end = row
  c_start = c_end = col

  if -1 < row-1: r_start -= 1
  if row+1 < m:  r_end += 1
  if -1 < col-1: c_start -= 1
  if col+1 < n: c_end += 1

  output = ""
  for i in range(r_start, r_end+1):
    for j in range(c_start, c_end+1):
      output += sketch[i][j]

    if j != c_end: output += "\n"
  
  print(f"Pos: {pos}", output, sep="\n")

def find_adjacent_cells(sketch, pos):
  m = len(sketch)
  n = len(sketch[0])
  row, col = pos
  connected = { val:None for val in ["above", "below", "left", "right"]}

  print_node(sketch, pos)

  if -1 < row-1: connected["above"] = (row-1, col)
  if row+1 < m:  connected["below"] = (row+1, col)
  if -1 < col-1: connected["left"]  = (row, col-1)
  if col+1 < n:  connected["right"] = (row, col+1)

  print(connected)
  return connected


def find_neighbor_pipes(sketch, pos):
  row, col = pos
  node = sketch[row][col]

  to_check = find_adjacent_cells(sketch, pos)
  neighbors = []

  def add_to_neighbors_if_exists_and_connects(neighbors, side, connecting_pieces):
    if not to_check[side]: return
    pos = to_check[side]
    row, col = pos
    # print(sketch[row][col], connecting_pieces)
    if sketch[row][col] not in connecting_pieces: return

    neighbors += [ pos ]

  if node == "S":
    add_to_neighbors_if_exists_and_connects(neighbors, "above", ["|", "F", "7"])
    add_to_neighbors_if_exists_and_connects(neighbors, "below", ["|", "L", "J"])
    add_to_neighbors_if_exists_and_connects(neighbors, "left", ["-", "F", "L"])
    add_to_neighbors_if_exists_and_connects(neighbors, "right", ["-", "J", "7"])
  elif node == "L":
    add_to_neighbors_if_exists_and_connects(neighbors, "above", ["|", "F", "7"])
    add_to_neighbors_if_exists_and_connects(neighbors, "right", ["-", "J", "7"])
  elif node == "J":
    add_to_neighbors_if_exists_and_connects(neighbors, "above", ["|", "F", "7"])
    add_to_neighbors_if_exists_and_connects(neighbors, "left", ["-", "F", "L"])
  elif node == "7":
    add_to_neighbors_if_exists_and_connects(neighbors, "below", ["|", "L", "J"])
    add_to_neighbors_if_exists_and_connects(neighbors, "left", ["-", "F", "L"])
  elif node == "F":
    add_to_neighbors_if_exists_and_connects(neighbors, "below", ["|", "L", "J"])
    add_to_neighbors_if_exists_and_connects(neighbors, "right", ["-", "J", "7"])

  print(f"Neighbors: {neighbors} for cell {pos}")
  return neighbors

def find_next_space(sketch, pos, visited):
  neighbors = find_neighbor_pipes(sketch, pos)
  print(pos, " ==> ", neighbors, visited) 
  for neighbor in neighbors:
    if neighbor not in visited: return neighbor

def calculate_furthest_point_from_start(sketch, start):
  left, right = find_neighbor_pipes(sketch, start)
  visited = { start }
  steps_from_start = 1

  while left != right:
    current = [ left, right ]
    for i in range(len(current)):
      elem = current[i]

      visited.add(elem)
      current[ i ] = find_next_space(sketch, elem, visited)

    left, right = current
    steps_from_start += 1
  
  return steps_from_start


if __name__ == "__main__":
  sketch = []
  start = None
  # with open("day_ten/example_one.txt") as file:
  with open("day_ten/example_two.txt") as file:
  # with open("day_ten.txt") as file:
    for row, line in enumerate(file):
      sketch_row = line.strip()
      for col, char in enumerate(sketch_row):
        if char == "S": start = (row, col)
      sketch += [ sketch_row ]

  # print(sketch)
  furthest_point_distance = calculate_furthest_point_from_start(sketch, start)
  print(furthest_point_distance)


  
