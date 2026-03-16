n = int(input())
cities = list(map(int, input().split()))

for i in range(len(cities)):
    try:
        minn = min(abs(cities[i] - cities[i - 1]), abs(cities[i] - cities[i + 1]))
    except IndexError:
        minn = abs(cities[i] - cities[i - 1])
    maxx = max(abs(cities[i] - cities[0]), abs(cities[i] - cities[-1]))

    print(minn, maxx)
