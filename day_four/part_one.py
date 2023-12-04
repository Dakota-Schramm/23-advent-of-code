import string

def calculate_score(winners, hand):
  matches = len(winners & hand)
  # print(matches, winners, " | ", hand)
  
  if matches == 0: return 0
  return 2 ** (matches - 1)

def parse_nums(text):
  cur = ''
  output = {int(char) for char in text.split(" ") if char not in ["", " ", "\n"]}

  return output

if __name__ == "__main__":
  total_score = 0

  with open("day_four.txt") as file:
    for line in file:
      first, rest = line.split(": ")
      winning, hand = rest.split(" | ")

      winning = parse_nums(winning)
      hand    = parse_nums(hand)

      total_score += calculate_score(winning, hand)

  print(total_score)





