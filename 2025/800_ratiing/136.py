n = int(input())
gift = list(map(int, input().split()))
order = [None] * n

for i in range(len(gift)):
    index = gift[i] - 1
    order[index] = str(i + 1)

print(" ".join(order))
