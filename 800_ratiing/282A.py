n = int(input())
x = 0

for _ in range(n):
  intruction = input()
  if "+" in intruction:
    x += 1

  else:
    x -= 1

print(x)