n, t = list(map(int, input().split(" ")))

minn = 10 ** (n - 1)
minn += t - (minn % t)
maxx = 10 ** (n)

if minn >= maxx:
    print(-1)
else:
    print(minn)
