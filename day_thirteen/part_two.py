def find_differences_between_lines(l1, l2):
  output = [0 if v1==v2 else 1 for v1, v2 in zip(l1, l2)]

  return sum(output)

def find_reflection_point_of_pattern(pattern):
  m = len(pattern)
  n = len(pattern[0])
  print(pattern, m, n)

  print(*pattern, sep="\n")
  row = 0
  while row < m-1:
    cur_row = pattern[ row ]
    next_row = pattern[ row + 1]

    smudges = find_differences_between_lines(cur_row, next_row)
    if 1 < smudges:
      row += 1
      continue

    i = row - 1
    j = row + 2
    while smudges < 2 and (-1 < i and j < m):
      diffs = find_differences_between_lines(pattern[i], pattern[j])

      smudges += diffs
      i -= 1
      j += 1
    print(row, smudges)
    if smudges == 1: return ["ROW", row] 

    row += 1
  
  col = 0
  while col < n-1:
    print(col)
    cur_col = [ row[col] for row in pattern ]
    next_col = [ row[col+1] for row in pattern ]

    smudges = find_differences_between_lines(cur_col, next_col)
    if 1 < smudges:
      col += 1
      continue

    i = col - 1
    j = col + 2

    while smudges < 2 and (0 < i and j < n):
      cur_col = [ row[i] for row in pattern ]
      next_col = [ row[j] for row in pattern ]
      diffs = find_differences_between_lines(cur_col, next_col)

      smudges += diffs
      i -= 1
      j += 1
    print(col, smudges)
    if smudges == 1: return ["COL", col]

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

  