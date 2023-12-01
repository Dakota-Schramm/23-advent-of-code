import string

print("hello world")

digits = set(string.digits)
def determine_calibration_value(text):
  n = len(text)
  left, right = 0, n - 1
  while text[left] not in digits:
    left += 1
  
  while text[right] not in digits:
    right -= 1

  return int(text[left] + text[right])

if __name__ == "__main__":
  output = 0

  with open("day_one.txt") as file:
    for item in file:
      output += determine_calibration_value(item)
  
  print(output)
