n,k = list(map(int, input().split(" ")))

for _ in range(k):
  if n % 10 > 0:
    n -= 1
  else:
    n /= 10

print(int(n))