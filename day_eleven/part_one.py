def draw_expanded_universe(universe):
  expanded_universe = []
  m = len(universe)
  n = len(universe[0])

  for line in universe:
    if line.count(".") == n: expanded_universe += [ line ]
    expanded_universe += [ line ]

  col = 0
  while col < n:
    cols = []
    for row in expanded_universe:
      cols += [ row[ col ] == "."]
    if all(cols): # fix this list
      for i in range(m):
        row = expanded_universe[i]

        str_arr = row.split()
        str_arr.insert(col, ".")
        row = "".join(str_arr) 

    col += 1
  
  # print(expanded_universe)
  return expanded_universe

if __name__ == "__main__":
  universe = []
  with open("day_eleven/example_one.txt") as file:
  # with open("day_eleven.txt") as file:
    for line in file:
      print(line)
      universe += [ line.strip() ]

  print(universe)
  expanded = draw_expanded_universe(universe)