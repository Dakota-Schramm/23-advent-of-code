import string

numbers = string.digits

def check_char_type(char):
  if char == ".":                  return "period"
  elif char in string.punctuation: return "punctuation"
  else:                            return "num"

def parse_number_in_schematic(schematic, type, pos):
  row, col = pos



def read_schematic(schematic):
  m = len(schematic)
  n = len(schematic[0])
  print(n, m)

  # def check_for_adjacent_numbers(row, column):
  #   center_space = schematic[row][column]
  #   num_to_add_for_space = 0

  #   print(row, column, center_space)
  #   for i in range(row-1, row+2):
  #     for j in range(column-1, column+2):
  #       if i == row and j == column: continue
  #       print(i, j, schematic[i][j])


  #       char_type = check_char_type(center_space)
  #       if char_type == "num":
  #         if i != row:
  #           pass
  #         else:
  #           num_str = str(center_space)
  #           if j == column-1:
  #             current = j
  #             while -1 < current and check_char_type(schematic[i][current]) == "num":
  #               num_str = schematic[i][current] + num_str
  #               current -= 1
  #           elif j == col+1:
  #             current = j
  #             while current < n and check_char_type(schematic[i][current] == "num"):
  #               num_str = num_str + schematic[i][current]
  #               current += 1

  #           num_to_add_for_space += int(num_str)

  part_number_sum = 0
  for line_num, line in enumerate(schematic):
    cur_num = ""

    if line_num in [0, m-1]: continue

    for col_num, char in enumerate(line):
      if col_num in [0, n-1]: continue
      cur_val = schematic[line_num][col_num]

      char_type = check_char_type(cur_val)
      if char_type == "num":
        cur_num += cur_val
  
  return part_number_sum
  

if __name__ == "__main__":
  schematic = []
  with open("day_three.txt") as file:
    for line in file:
      schematic += [line]
  
  output = read_schematic(schematic)
  print(output)
  
  