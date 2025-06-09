n,h = list(map(int, input().split(" ")))
friends = list(map(int, input().split(" ")))
count = 0

for height in friends:
  if height > h:
    count += 2
  else:
    count += 1

print(count)