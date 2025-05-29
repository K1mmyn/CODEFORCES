n = int(input())
coins = sorted(list(map(int, input().split(' '))))[::-1]
count = 0
x = 0

min_value = sum(coins) // 2

for i in range(n):
  if x <= min_value:
    x += coins[i]
    count += 1

print(count)



