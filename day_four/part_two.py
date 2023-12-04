import string
from collections import deque

# seems to be working correctly
def calculate_matches(winners, hand):
  matches = len(winners & hand)
  return matches

def parse_nums(text):
  output = {int(char) for char in text.split(" ") if char not in ["", " ", "\n"]}
  return output

def calculate_scorecard_count(file_input):
  n = len(file_input)
  total_scratched = 0
  card_matches = [-1] * n
  to_scratch = deque([val for val in range(n)])

  while len(to_scratch):
    idx = to_scratch.popleft()
    total_scratched += 1
    winning, hand = file_input[idx]

    matches = card_matches[idx]
    if matches == -1: 
      matches = calculate_matches(winning, hand) 
      card_matches[idx] = matches

    for i in range(1, matches+1):
      next_card = idx + i
      if n <= next_card: break
      to_scratch.append(next_card)
  
  return total_scratched

if __name__ == "__main__":
  file_input = []
  with open("day_four.txt") as file:
  # with open("day_four/two_example.txt") as file:
    for line in file:
      _, rest = line.split(": ")
      winning, hand = rest.split(" | ")

      winning = parse_nums(winning)
      hand    = parse_nums(hand)

      file_input.append([winning, hand])

  total_scratchcards = calculate_scorecard_count(file_input)
  print(total_scratchcards)

