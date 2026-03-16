n = int(input())

res = "maybe"

prev = float("inf")
flag1 = False
flag2 = False

for i in range(n):
    a, b = list(map(int, input().split(" ")))

    if a != b:
        flag1 = True
        break
    elif a > prev:
        flag2 = True

    prev = a

if flag1:
    print("rated")
elif flag2:
    print("unrated")
else:
    print("maybe")
