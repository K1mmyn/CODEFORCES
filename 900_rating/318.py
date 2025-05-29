import math
n, k = list(map(int, input().split(" ")))

n = math.ceil(n/2) 
if k <= n:
  print((2*k) - 1)
else:
  k = k - n
  print((2 * k))