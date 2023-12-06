def convert_seeds_to_locations(seeds, maps):
  locations = []

  types = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location"
  ]

  # print(seeds)
  for seed in seeds:
    current = seed
    for idx, interval_map in enumerate(maps):
      # print(f"{types[idx]}: {current}")
      for interval in interval_map.keys():
        start, end = interval
        if start <= current and current < end:
          diff = abs(start - current)
          dest_start = interval_map[interval][0] 
          # print(start, end, current, dest_start, diff, current)
          current = dest_start + diff
          break
    #   print("interval_map: ", interval_map)
    # print("Location: ", current)
    locations += [current]
  
  return locations

if __name__ == "__main__":
  seeds = []
  seed_to_soil = {}
  soil_to_fertilizer = {}
  fertilizer_to_water = {}
  water_to_light = {}
  light_to_temperature = {}
  temperature_to_humidity = {}
  humidity_to_location = {}

  with open("day_five.txt") as file:
  # with open("day_five/example_one.txt") as file:
    cur_type = ""
    for idx, line in enumerate(file):
      if idx == 0:
        _, nums = line.split(": ")
        seeds = [int(num) for num in nums.split(" ") if num not in ["\n"]]
        continue

      if line == "\n":
        cur_type = "" 
        continue
      elif line[-2] == ":":
        cur_type = line[:-2]
        continue

      nums = [int(num) for num in line.split(" ") if num not in ["", "\n"]]
      dest_range_start, source_range_start, range_length = nums
      source_interval = (source_range_start, source_range_start + range_length)
      dest_interval = (dest_range_start, dest_range_start + range_length)

      if cur_type == "seed-to-soil map":
        seed_to_soil[ source_interval ] = dest_interval
      elif cur_type == "soil-to-fertilizer map":
        soil_to_fertilizer[ source_interval ] = dest_interval
      elif cur_type == "fertilizer-to-water map":
        fertilizer_to_water[ source_interval ] = dest_interval
      elif cur_type == "water-to-light map":
        water_to_light[ source_interval ] = dest_interval
      elif cur_type == "light-to-temperature map":
        light_to_temperature[ source_interval ] = dest_interval
      elif cur_type == "temperature-to-humidity map":
        temperature_to_humidity[ source_interval ] = dest_interval
      elif cur_type == "humidity-to-location map":
        humidity_to_location[ source_interval ] = dest_interval
    
    interval_maps = [
      seed_to_soil,
      soil_to_fertilizer,
      fertilizer_to_water,
      water_to_light,
      light_to_temperature,
      temperature_to_humidity,
      humidity_to_location
    ]
    print(interval_maps)

    locations = convert_seeds_to_locations(seeds, interval_maps)
    min_location = min(locations)
    print(locations, min_location)




