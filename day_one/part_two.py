import string

print("hello world")

digits = set(string.digits)
words = [
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine"
]

def determine_calibration_value(text):
  n = len(text)
  left_idx, right_idx = 0, n - 1
  left = right = None

  def number_word_found(index):
    for word in words:
      word_len = len(word)
      word_from_index = text[index:index+word_len]

      if word == word_from_index:
        return word

    return None

  while left_idx < n:
    if text[left_idx] in digits:
      left = int(text[left_idx])
      break

    found = number_word_found(left_idx)
    if found:
      left = words.index(found) + 1
      break

    left_idx += 1

  while -1 < right_idx:
    if text[right_idx] in digits:
      right = int(text[right_idx])
      break

    found = number_word_found(right_idx)
    if found:
      right = words.index(found) + 1
      break

    right_idx -= 1
  
  print(text, left, right)
  return int(f"{left}{right}")

if __name__ == "__main__":
  output = 0

  with open("day_one.txt") as file:
    for item in file:
      output += determine_calibration_value(item)
  
  print(output)
