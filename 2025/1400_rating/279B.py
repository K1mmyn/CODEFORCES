n, t = list(map(int, input().split()))
books = list(map(int, input().split()))

maxx = 0
length = 0
total = 0
l = 0

for r in range(len(books)):
    total += books[r]
    length += 1

    while total > t:
        total -= books[l]
        length -= 1
        l += 1

    maxx = max(length, maxx)

print(maxx)
