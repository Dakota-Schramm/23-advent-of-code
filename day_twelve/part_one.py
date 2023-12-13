def calculate_possible_arrangements(spring_rows, contiguous_broken_springs):
  print(spring_rows, contiguous_broken_springs)

  arrangements = []
  for row, string in zip(spring_rows, contiguous_broken_springs):
    arrangement = 0
    cur_cont_broken_springs = [0] * len(string)
    cur_idx = 0
    cur_springs = 0

    groups = [char for char in row.split(".") if char not in [""]]

    print(groups)
    arrangements += [ arrangement ]

  return arrangements

if __name__ == "__main__":
  spring_rows = []
  contiguous_broken_springs = []

  with open("day_twelve/example_one.txt") as file:
  # with open("day_twelve.txt") as file:
    for line in file:
      spring_row, contiguous_broken_strings = line.split(" ")
      spring_rows += [ spring_row ]
      contiguous_broken_springs.append(
        [ int(spring) for spring in contiguous_broken_strings.split(",")]
      )
  
  arrangements = calculate_possible_arrangements(spring_rows, contiguous_broken_springs)
  total = sum(arrangements)
  print(arrangements, total, sep="\n")


