n = int(input())
wires = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = list(map(int, input().split()))
    x = x - 1

    right = wires[x] - y
    left = y - 1
    wires[x] = 0

    if x - 1 >= 0:
        wires[x - 1] += left

    if x + 1 <= n - 1:
        wires[x + 1] += right

print("\n".join(str(wire) for wire in wires))
