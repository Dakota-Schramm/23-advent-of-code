color_map = {
  "red": 0,
  "green": 1,
  "blue": 2
}

def get_power_of_minimum_set(counts):
  red_min = green_min = blue_min = 0

  for count in counts:
    red, blue, green = [int(value) for value in count]

    red_min = max(red_min, red)
    green_min = max(green_min, green)
    blue_min = max(blue_min, blue)
  
  output = red_min * green_min * blue_min
  print("counts: ", counts)
  print(red_min, green_min, blue_min, output)

  return output

def parse_line(line):
  sets = line.split("; ")
  _, set_str = sets[0].split(": ")

  new_sets = [set_str,]
  new_sets.extend(sets[1:])
  output_sets = []

  for new_set in new_sets:
    colors = new_set.split(", ")
    to_add = [0, 0, 0]
    for color in colors:
      count, style = color.split(" ")
      index = color_map[style.strip("\n")]
      to_add[index] = count

    output_sets += [to_add]
      
  return output_sets

if __name__ == "__main__":
  power_sum = 0

  with open("day_two.txt") as file:
    for line in file:
      sets = parse_line(line)
      power_sum += get_power_of_minimum_set(sets)
  
  print(power_sum)

