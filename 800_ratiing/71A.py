
n = int(input())

for x in range(n):
  word = input()
  
  if len(word) <= 10:
    print(word)
  else:
    print(f"{word[0]}{len(word[1:-1])}{word[-1]}")