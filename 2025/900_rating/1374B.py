import math
t = int(input())

for x in range(t):
  n = int(input())
  count = 0
  
  while True:

    if n == 1:
      print(count)
      break
    floor = n // 6
    ceil = n / 6

    if floor == ceil:
      n //= 6
      count += 1
    else:
      temp = n % 6
      if temp == 4 or temp == 5 or temp == 2:
        print(-1)
        break
      n *= 2
      count += 1
    



