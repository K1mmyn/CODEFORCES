n,m = list(map(int, input().split(" ")))
puzzles = list(map(int, input().split(" ")))
difference = []

l_pointer = 0
r_pointer = n - 1

for x in range(len(puzzles)):
  for y in range(len(puzzles) - 1 - x):
    if puzzles[y] > puzzles[y + 1]:
      puzzles[y], puzzles[y + 1] = puzzles[y+1], puzzles[y]

for i in range(m-n + 1):
  difference.append(puzzles[r_pointer + i] - puzzles[l_pointer + i])

print(min(difference))