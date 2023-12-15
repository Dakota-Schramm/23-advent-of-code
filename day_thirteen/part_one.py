def find_reflection_point_of_pattern(pattern):
  m = len(pattern)
  n = len(pattern[0])

  print(*pattern, sep="\n")
  row = 0
  while row < m-1:
    cur_row = pattern[ row ]
    next_row = pattern[ row + 1]

    if cur_row == next_row:
      i = row
      j = row + 1

      while pattern[i] == pattern[j]:
        i -= 1
        j += 1
        if i < 0 or m <= j: return ["ROW", row]
  
    row += 1
  
  col = 0
  while col < n-1:
    cur_col = [ row[col] for row in pattern ]
    next_col = [ row[col+1] for row in pattern ]

    if cur_col == next_col:
      i = col 
      j = col + 1

      while [ row[i] for row in pattern ] == [ row[j] for row in pattern ]:
        i -= 1
        j += 1
        if i < 0 or n <= j: return ["COL", col]

    col += 1
  
  raise Exception("Reflection point not found")

def summarize_pattern(pattern):
  reflect_type, cell_before_line = find_reflection_point_of_pattern(pattern)
  print(reflect_type, cell_before_line)
  one_indexed = cell_before_line + 1
  if reflect_type == "ROW":
    return 100 * one_indexed
  else:
    return one_indexed

def sum_summaries(patterns):
  summaries = [summarize_pattern(pattern) for pattern in patterns ]
  print(summaries)
  return sum(summaries)

if __name__ == "__main__":
  patterns = []
  # with open("day_thirteen/example_one.txt") as file:
  with open("day_thirteen.txt") as file:
    pattern = []
    for line in file:
      if len(line.strip()) != 0: pattern += [ line.strip() ]
      else: 
        if pattern: patterns += [ pattern ]
        pattern = []
    if pattern: patterns += [ pattern ]
  
  # print(patterns)
  total = sum_summaries(patterns)
  print(total)

  