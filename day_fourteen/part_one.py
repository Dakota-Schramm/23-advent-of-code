CUBE_ROCK = "#"
ROUNDED_ROCK = "O"
EMPTY = "."

def print_dish_map(dish_rocks):
  for row in dish_rocks:
    print("".join(row))

def roll_rocks_north(dish_rocks):
  m = len(dish_rocks)
  n = len(dish_rocks[0])

  rocks_after_slide = [ list(row) for row in dish_rocks ]
  empty, rounded = 0, 0
  cur_idx = 0

  for col_idx in range(n):
    single_col = [ row[col_idx] for row in rocks_after_slide ]
    for row in single_col:
      if row == ".":   empty += 1
      elif row == "O": rounded += 1
      else:
        while 0 < rounded:
          rocks_after_slide[cur_idx][col_idx] = ROUNDED_ROCK
          cur_idx += 1
          rounded -= 1
        while 0 < empty:
          rocks_after_slide[cur_idx][col_idx] = EMPTY
          cur_idx += 1
          empty -= 1

    if rounded:
      while 0 < rounded:
        rocks_after_slide[cur_idx][col_idx] = ROUNDED_ROCK
        cur_idx += 1
        rounded -= 1
      while 0 < empty:
        rocks_after_slide[cur_idx][col_idx] = EMPTY
        cur_idx += 1
        empty -= 1

    empty = 0
    cur_idx = 0
    

  return rocks_after_slide

def calculate_load_on_north_support_beams(dish_rocks):
  total_load = 0
  print(dish_rocks)

  return total_load 

if __name__ == "__main__":
  dish_rocks = []
  with open("day_fourteen/example_one.txt") as file:
  # with open("day_fourteen.txt") as file:
    for line in file:
      dish_rocks.append([ char for char in line.strip() ])
  
  dish_rocks_rolled = roll_rocks_north(dish_rocks)

  print_dish_map(dish_rocks)
  print("=" * 20)
  print_dish_map(dish_rocks_rolled)
  total_load = calculate_load_on_north_support_beams(dish_rocks_rolled)
  print(total_load)
