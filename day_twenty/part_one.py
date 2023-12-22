class Solution:
  def __init__(self, module_connections, flip_flops, conjunctions, broadcaster):
    self.module_types = module_connections
    self.flip_flops = flip_flops
    self.conjunctions = conjunctions
    self.broadcaster = broadcaster
    self.pulses = [] # { module, type }

  def calculate_magic_pulse_number(self):
    low = high = 0
    for _ in range(1000):
      self._send_button_pulse()
      pulses = self._process_pulses()
      low += pulses[0]
      high += pulses[1]

    return low * high

  def pulse_print(self, module, p_type, destination):
    print(f"{module} -{p_type}-> {destination}")

  def _process_pulses(self):
    low = 0
    high = 0

    while len(self.pulses):
      pulse = self.pulses.pop(0)
      if pulse["type"] == "off": low += 1 
      else:                      high += 1

      module = pulse["module"]
      if module == "broadcaster":
        self._process_broadcaster_pulse()
        continue

      module_type = self.module_types[module]
      if module_type == "flip-flops":    self._process_flip_flop_pulse(pulse)
      elif module_type == "conjunction": self._process_conjunction_pulse(pulse)
    
    return [low, high]

  def _process_broadcaster_pulse(self):
    for dest_module in self.broadcaster:
      self.pulses.append({
        "module": dest_module,
        "type": "low"
      })
  
  def _process_flip_flop_pulse(self, pulse):
    p_type = pulse["type"]
    if p_type == "high": return 

    if self.flip_flops[module] == "off":
      self.flip_flops[module] = "on"
      for dest_module in self.module_connections[module]:
        pulse_print(module, "low", dest_module) 
        self.pulses.append({
          "module": dest_module,
          "type": "low"
        })
    else:
      self.flip_flops[module] = "off"
      for dest_module in self.module_connections[module]:
        pulse_print(module, "high", dest_module) 
        self.pulses.append({
          "module": dest_module,
          "type": "high"
        })

  def _process_conjunction_pulse(self, pulse):
    index = None
    for idx, c in enumerate(self.conjunctions):
      if c[0] == module: index = idx
    self.conjunctions[index] = (module, p_type)

    allHighPulses = True
    for c in self.conjunctions:
      if c[1] == "low": allHighPulses = False

    for dest_module in self.module_connections[module]:
      pulse_type = "low" if allHighPulses else "high"
      self.pulse_print(module, pulse_type, dest_module) 
      self.pulses.append({
        "module": dest_module,
        "type": pulse_type
      })

  def _send_button_pulse(self):
    self.pulse_print("button", "low", "broadcaster")
    self.pulses.append({ "module": "broadcaster", "type": "low" })
  


if __name__ == "__main__":
  module_connections = {}

  flip_flops = {}
  conjunctions = {}
  broadcaster = []

  with open("day_twenty/example_one.txt") as file:
  # with open("day_twenty/example_two.txt") as file:
  # with open("day_twenty.txt") as file:
    for line in file:
      source_module, dest_module = [ val.strip() for val in line.split(" -> ") ]
      dest_modules = dest_module.split(", ") if 1 < len(dest_module) else [dest_module]

      if source_module == "broadcaster":
        broadcaster = list(dest_modules)
        continue

      module = source_module[1:]
      if source_module[0] == "%": 
        module_connections[module] = list(dest_modules)
        flip_flops[module] = "off"
      elif source_module[0] == "&": 
        module_connections[module] = list(dest_modules)
        conjunctions[module] = [ (val, "off") for val in dest_modules ]

  print("MT: ", module_connections)
  print("FF: ", flip_flops)
  print("C: ", conjunctions)
  print("B: ", broadcaster)
  solution = Solution(module_connections, flip_flops, conjunctions, broadcaster)
  output = solution.calculate_magic_pulse_number()
  print(output)
