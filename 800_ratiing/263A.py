row1 = list(map(int, input().split(" ")))
row2 = list(map(int, input().split(" ")))
row3 = list(map(int, input().split(" ")))
row4 = list(map(int, input().split(" ")))
row5 = list(map(int, input().split(" ")))

matrix = [row1, row2, row3, row4, row5]

row_with_one = []
count = 0


for i in range(5):
  if 1 in matrix[i]:
    index = matrix[i].index(1)
    row_with_one = [index, i]

for i in range(2):
  if row_with_one[0] == 2:
    continue
  if row_with_one[0] > 2:
    row_with_one[0] = row_with_one[0] - 1
    count += 1

  else:
    row_with_one[0] = row_with_one[0] + 1
    count += 1

for i in range(2):
  if row_with_one[1] == 2:
    continue
  if row_with_one[1] > 2:
    row_with_one[1] = row_with_one[1] - 1
    count += 1
  else:
    row_with_one[1] = row_with_one[1] + 1
    count += 1    

print(count)
    