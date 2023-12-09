def moves_to_navigate_from_AAA_to_ZZZ(instructions, adj_graph):
  moves = 0
  current = "AAA"
  instruct_len = len(instructions)

  while current != "ZZZ":
    next_move_idx = moves % instruct_len
    next_move = instructions[ next_move_idx ]

    neighbor_idx = 0 if next_move == "L" else 1
    current = adj_graph[ current ][ neighbor_idx ]
    moves += 1

  return moves

if __name__ == "__main__":
  instructions = ""
  adj_graph = {}
  with open("day_eight.txt") as file:
  # with open("day_eight/example_one.txt") as file:
  # with open("day_eight/example_two.txt") as file:
    for idx, line in enumerate(file):
      print(line)

      if idx == 0:
        instructions = line.strip()
        continue
      elif idx == 1: continue

      node, neighbors = line.split(" = ")
      left, right = neighbors[1:-2].split(", ")
      adj_graph[node] = (left, right)
  print(instructions, adj_graph)
  total = moves_to_navigate_from_AAA_to_ZZZ(instructions, adj_graph)
  print(total)
      

      
