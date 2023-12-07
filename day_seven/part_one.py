from collections import Counter
from functools import cmp_to_key

CARD_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
FIRST_ORDERING = ["5oak", "4oak", "FH", "3OAK", "2P", "1P", "HC"]

def calculate_first_ordering(hand):
  # Five of a kind, where all five cards have the same label: AAAAA
  # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
  # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
  # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
  # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
  # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
  # High card, where all cards' labels are distinct: 23456
  card_counts = Counter(hand[0])
  distinct_cards = len(card_counts)

  print(card_counts)
  if distinct_cards == 1:     return FIRST_ORDERING[0]

  vals = list(card_counts.values())
  if distinct_cards == 2:
    if 4 in vals:             return FIRST_ORDERING[1]
    else:                     return FIRST_ORDERING[2]
  elif distinct_cards == 3:
    print(card_counts)
    if 3 in vals:             return FIRST_ORDERING[3]
    if vals.count(2) == 2:    return FIRST_ORDERING[4]
  elif distinct_cards == 4:
    if 2 in vals:             return FIRST_ORDERING[5]
  elif distinct_cards == 5:   return FIRST_ORDERING[6]

def calculate_second_ordering(hand_winning1, hand_winning2):
  # If two hands have the same type, a second ordering rule takes effect. Start 
  # by comparing the first card in each hand. If these cards are different, the 
  # hand with the stronger first card is considered stronger. If the first card 
  # in each hand have the same label, however, then move on to considering the 
  # second card in each hand. If they differ, the hand with the higher second 
  # card wins; otherwise, continue with the third card in each hand, then 
  # the fourth, then the fifth.
  hand1, _ = hand_winning1
  hand2, _ = hand_winning2
  for card1, card2 in zip(hand1, hand2):
    val1 = CARD_ORDER.index(card1)
    val2 = CARD_ORDER.index(card2)
    if val1 == val2: continue
    return val2 - val1

def order_hands(hands):
  first_ordering_pile = { order:[] for order in FIRST_ORDERING }
  for hand in hands:
    first_ordering_pile[ calculate_first_ordering(hand) ] += [hand]
  # print(first_ordering_pile)

  ordered_hand = []
  for hand_type, hands_awarded_type in reversed(first_ordering_pile.items()):
    print(hand_type,hands_awarded_type, ordered_hand)
    n = len(hand_type)
    if n == 0: continue
    elif n == 1: ordered_hand += [ hands_awarded_type[0] ]
    else:        ordered_hand.extend(sorted(hands_awarded_type, key=cmp_to_key(calculate_second_ordering)))
  
  return ordered_hand

def calculate_camel_case_winnings(hands, winnings):
  hand_winnings = zip(hands, winnings)
  hand_winnings = order_hands(hand_winnings)
  print(hand_winnings)

  results = [winning[1] * (i+1) for i, winning in enumerate(hand_winnings)]
  return sum(results)

if __name__ == "__main__":
  hands, winnings = [], []
  with open("day_seven.txt") as file:
  # with open("day_seven/example_one.txt") as file:
    for line in file:
      hand, winning = line.split(" ")
      hands    += [ hand ]
      winnings += [ int(winning) ]
  print(hands, winnings)
  total_winnings = calculate_camel_case_winnings(hands, winnings)
  print(total_winnings)
  