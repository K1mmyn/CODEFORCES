n, m = list(map(int, input().split(" ")))
tvs = list(map(int, input().split(" ")))

for x in range(len(tvs)):
  for y in range(x + 1, len(tvs)):
    if tvs[x] > tvs[y]:
      tvs[x], tvs[y] = tvs[y], tvs[x]

profit = 0

for x in range(1,m + 1):
  profit_x = sum(tvs[:x])
  if profit_x < 0 and abs(profit_x) > profit:
    profit = abs(profit_x)

print(profit)