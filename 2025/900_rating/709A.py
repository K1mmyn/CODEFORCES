n, b, d = list(map(int, input().split()))
oranges = list(map(int, input().split()))

waste = 0
count = 0

for o in oranges:
    if o > b:
        continue
    if o + waste > d:
        waste = 0
        count += 1
    else:
        waste += o

print(count)
