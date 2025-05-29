import math
n = int(input())

for i in range(n):
  s = int(input())
  s = math.sqrt(s)
  if s % 1 != 0:
    print(-1)
    continue

  print(math.floor(s/2), math.ceil(s/2))