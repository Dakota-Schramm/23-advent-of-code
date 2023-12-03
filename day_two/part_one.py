color_map = {
  "red": 0,
  "green": 1,
  "blue": 2
}

def check_if_valid_set(counts):
  for count in counts:
    red, green, blue = [int(value) for value in count]
    if 12 < red: return False
    if 13 < green: return False
    if 14 < blue: return False
  return True

def parse_line(line):
  sets = line.split("; ")
  game_str, set_str = sets[0].split(": ")
  _, game_id = game_str.split(" ")

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
      
  return [
    game_id,
    output_sets
  ]

if __name__ == "__main__":
  id_sum = 0

  with open("day_two.txt") as file:
    for line in file:
      game_id, sets = parse_line(line)

      if check_if_valid_set(sets):
        id_sum += int(game_id)
  
  print(id_sum)

