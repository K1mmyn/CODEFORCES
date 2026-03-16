n, h = list(map(int, input().split()))
a = list(map(int, input().split()))

count = len(a)

for num in a:
    if num > h:
        count += 1

print(count)
