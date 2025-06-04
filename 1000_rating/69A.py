n = int(input())
total_forces = 0

for x in range(n):
  forces = list(map(int, input().split(" ")))
  total_forces += sum(forces)

if total_forces == 0:
  print('YES')
else:
  print("NO")