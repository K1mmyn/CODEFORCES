n = int(input())
p = set(map(int, input().split(" ")[1:]))
q = set(map(int, input().split(" ")[1:]))


res = "I become the guy."

for i in range(1, n + 1):
    if i not in p and i not in q:
        res = "Oh, my keyboard!"
        break

print(res)
