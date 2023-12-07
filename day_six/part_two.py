
def calculate_num_of_ways_to_win_race(time, distance):
  left = right = 0
  i = 0
  j = time
  for time_to_charge in range(time):
    speed = time_to_charge
    time_remaining = time - time_to_charge
    current_race_distance = time_remaining * speed

    print(distance, current_race_distance)
    if distance < current_race_distance:
      ways += 1

  return ways

if __name__ == "__main__":
  times = "" 
  distances = ""
  # with open("day_six.txt") as file:
  with open("day_six/example_one.txt") as file:
    for line in file:
      title, rest = line.split(":")

      to_add = ""
      for char in rest:
        if char not in [" ", "\n"]:
          to_add += char

      if title == "Time": time = int(to_add)
      elif title == "Distance": distance = int(to_add)
  
  print(times, distances)
  print("-----")
  race_ways = calculate_num_of_ways_to_win_race(time, distance)
  print(race_ways)
  




