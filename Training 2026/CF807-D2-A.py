n = int(input())

res = "unrated"
for _ in range(n):
    a, b = list(map(int, input().split(" ")))
    if a != b:
        res = "rated"
        break

print(res)
