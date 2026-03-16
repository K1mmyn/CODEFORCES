n = int(input())
days = list(map(int, input().split(" ")))
longest = 1
count = 1


for x in range(len(days) - 1):
  if days[x] <= days[x + 1]:
    count += 1
    if count > longest:
      longest = count
  else:
    count = 1


print(longest)