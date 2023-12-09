def is_endpath(node):
  return node[-1] == "Z"

def number_of_moves_for_ghost_to_nodes_ending_with_z(instructions, adj_graph):
  current = [node for node in adj_graph.keys() if node[-1] == "A"]
  
  instruct_len = len(instructions)

  # [n for n in current if n[-1] == "Z"]
  # calculating with a while loop is too expensive
  # we're looking at a LCD problem, so find
  while len( list(filter( is_endpath, current )) ) != len(current):
    next_move_idx = moves % instruct_len
    next_move = instructions[ next_move_idx ]
    print(moves, current, next_move)

    neighbor_idx = 0 if next_move == "L" else 1
    next_nodes = []
    for node in current:
      next_nodes += [ adj_graph[ node ][ neighbor_idx ] ]
    current = next_nodes
    moves += 1
  print("END", moves, current)

  return moves

if __name__ == "__main__":
  instructions = ""
  adj_graph = {}
  with open("day_eight.txt") as file:
  # with open("day_eight/example_three.txt") as file:
    for idx, line in enumerate(file):
      # print(line)

      if idx == 0:
        instructions = line.strip()
        continue
      elif idx == 1: continue

      node, neighbors = line.split(" = ")
      left, right = neighbors[1:-2].split(", ")
      adj_graph[node] = (left, right)
  total = number_of_moves_for_ghost_to_nodes_ending_with_z(instructions, adj_graph)
  print(total)
      

      
