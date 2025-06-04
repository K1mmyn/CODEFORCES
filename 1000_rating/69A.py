n = int(input())
sum_x = 0
sum_y = 0
sum_z = 0

for x in range(n):
  forces = list(map(int, input().split(" ")))
  sum_x += forces[0]
  sum_y += forces[1]
  sum_z += forces[2]

if sum_x == 0 and sum_y == 0 and sum_z == 0:
  print('YES')
else:
  print("NO")