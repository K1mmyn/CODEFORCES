import math
n = int(input())
groups = list(map(int, input().split(" ")))
groups = sorted(groups)
count = 0

while len(groups) and groups[-1] == 4:
  count += 1
  groups.pop()

while len(groups) and groups[-1] == 3:
  if groups[0] == 1:
    groups.pop(0)
  
  count += 1
  groups.pop()


print(count + (math.ceil(sum(groups) / 4)))