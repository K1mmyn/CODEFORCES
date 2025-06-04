string = input()
word = []

for char in string:
  if len(word) == 5:
    break
  if char == "h" and len(word) == 0:
    word.append(char)
  elif char == "e" and len(word) == 1:
    word.append(char)
  elif char == "l" and (len(word) == 2 or len(word) == 3):
    word.append(char)
  elif char == "o" and len(word) == 4:
    word.append(char)
  
word = "".join(word)

if word == "hello":
  print("YES")
else:
  print("NO")