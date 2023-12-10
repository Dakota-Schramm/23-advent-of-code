def find_next_value_of_history(history):
  history_sequence = [ history ]
  current_history_sequence = history

  while not all([val == 0 for val in current_history_sequence]):
    next_seq = []
    for i in range(len(current_history_sequence) - 1):
      diff = current_history_sequence[ i + 1 ] - current_history_sequence[ i ]
      next_seq += [ diff ]
    
    history_sequence += [ next_seq ]
    current_history_sequence = next_seq
  
  print(history_sequence)
  n = len(history_sequence)
  for i in reversed(range(n)):
    if i == n-1:
      history_sequence[i] += [0]
    else:
      diff      = history_sequence[ i + 1 ][-1]
      new_value = history_sequence[ i ][-1] + diff
      history_sequence[ i ] += [ new_value ]
  
  return history_sequence[0][-1]
    
def sum_extrapolated_oasis_histories(histories):
  predicted_histories = [ (find_next_value_of_history(h)) for h in histories ]
  print(predicted_histories)
  return sum(predicted_histories)

if __name__ == "__main__":
  oasis_histories = []
  with open("day_nine.txt") as file:
  # with open("day_nine/example_one.txt") as file:
    for line in file:
      value_history = [int(val) for val in line.split(" ")]
      oasis_histories += [value_history]
  print(oasis_histories)
  total = sum_extrapolated_oasis_histories(oasis_histories)
  print("TOTAL: ", total)
