n = int(input())
stones = list(input())
count = 0

for x in range(n - 1):
  if stones[x] == stones[x + 1]:
    count += 1

print(count)
