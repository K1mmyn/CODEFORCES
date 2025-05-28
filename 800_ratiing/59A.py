word = list(input())
uppercase = 0

for char in word:
  if char == char.upper():
    uppercase += 1

lowercase = len(word) - uppercase 

if lowercase >= uppercase:
  print("".join(word).lower())
  
else:
  print("".join(word).upper())
