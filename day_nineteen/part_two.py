WORKFLOWS = { 'a', 'r', }

class Solution:
  def __init__(self, workflows, parts):
    self.workflows = workflows
    self.parts = parts
  
  def get_ratings_for_accepted_parts(self):
    accepted_parts = self._determine_accepted_parts()
    ratings = self._calculate_ratings(accepted_parts)

    print("Accepted rating sum: ", ratings)
  
  def _determine_accepted_parts(self):
    current_step = "in"
    accepted = []
    
    print("parts: ", self.parts)
    for part in self.parts:
      while current_step not in ["A", "R"]:
        # print(f"{part} | {current_step}")
        current_step = self._determine_workflow_path(part, workflows[current_step])

      if current_step == "A": accepted.append(part) 
      current_step = "in"

    print('done')
    return accepted
  
  def _determine_workflow_path(self, part, workflow):
    for step in workflow:
      if len(step) == 2:
        check, b_if = step
        trait, op, val = check[0], check[1], check[2:] 
        boolean = eval(f"{ part[trait] }{ op }{ val }")
        if boolean: return b_if 
      else: return step[0]

  def _calculate_ratings(self, parts):
    total_rating = 0
    for part in parts:
      part_total = 0
      for val in part.values():
        part_total += val

      print(f"adding {part_total} for part {part}")
      total_rating += part_total
    
    return total_rating

if __name__ == "__main__":
  workflows = {}
  parts = []
  # with open("day_nineteen/example_one.txt") as file:
  with open("day_nineteen.txt") as file:
    isWorkflow = True
    for line in file:
      to_add = line.strip()
      if len(to_add) == 0: isWorkflow = False
      elif isWorkflow:
        workflow = []
        wf, rest = to_add.split("{")
        boolean = [ val.strip("}") for val in rest.split(",") ]

        workflows[wf] = []
        for b in boolean:
          b_bool, b_if, b_else = None, None, None
          first = b.split(":")

          if len(first) == 2: workflows[wf].append(first)
          else:               workflows[wf] += [ first ]

      else:
        vals = [ val.strip("{}") for val in to_add.split(",") ]
        part = {}
        for val in vals:
          k, v = val.split("=")
          part[k] = int(v)
        parts += [ part ]

  solution = Solution(workflows, parts)
  ratings = solution.get_ratings_for_accepted_parts()
