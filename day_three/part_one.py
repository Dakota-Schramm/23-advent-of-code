import string

numbers = string.digits

def check_char_type(char):
  if char == ".":                  return "period"
  elif char in string.punctuation: return "punctuation"
  else:                            return "num"

def find_symbol_adjacent_nums(schematic):
  n = len(schematic)

  adjacent_to_symbol = set()
  for row, line in enumerate(schematic):
    for col, char in enumerate(line):
      cell = (row, col)
      cur_val = schematic[row][col]

      char_type = check_char_type(cur_val)
      if char_type == "num":
        
        for r in range( row-1, min(row+2, n) ):
          for c in range( col-1, min(col+2, n) ):
            if r == row and c == col: continue
            if check_char_type( schematic[r][c] ) == "punctuation": adjacent_to_symbol.add(cell) 
  
  return adjacent_to_symbol

def calculate_part_num_total(schematic, num_coords):
  total_part_num = 0

  for row, line in enumerate(schematic):
    cur_num = ""
    is_part_num = False

    for col, char in enumerate(line):
      current_cell = (row, col)

      char_type = check_char_type(char)
      if char_type == "num":
        cur_num += char
        if current_cell in num_coords: is_part_num = True
      else:
        if is_part_num:
          print(cur_num)
          to_add = int(cur_num)
          total_part_num += to_add
        cur_num = ""
        is_part_num = False
    
    cur_num = cur_num.strip("\n")
    print(cur_num)
    if cur_num: total_part_num += int(cur_num)

  return total_part_num
  
if __name__ == "__main__":
  schematic = []
  with open("day_three.txt") as file:
  # with open("day_three/one_example.txt") as file:
    for line in file:
      schematic += [line]
  
  num_coords = find_symbol_adjacent_nums(schematic)
  part_num_total = calculate_part_num_total(schematic, num_coords)

  print(part_num_total)