
def calculate_num_of_ways_to_win_race(times, distances):
  race_ways = []
  for time, distance in zip(times, distances):
    ways = 0
    speed = 0
    for time_to_charge in range(time):
      speed = time_to_charge
      time_remaining = time - time_to_charge
      current_race_distance = time_remaining * speed

      print(distance, current_race_distance)
      if distance < current_race_distance:
        ways += 1
    race_ways += [ways]

  return race_ways

if __name__ == "__main__":
  times = []
  distances = []
  with open("day_six.txt") as file:
  # with open("day_six/example_one.txt") as file:
    for line in file:
      title, rest = line.split(":")

      nums = [int(val) for val in rest.split(" ") if val not in ["\n", ""]]
      if title == "Time": times = nums
      elif title == "Distance": distances = nums
  
  print(times, distances)
  print("-----")
  race_ways = calculate_num_of_ways_to_win_race(times, distances)
  output = 1
  for way in race_ways: output *= way
  print(output)
  




