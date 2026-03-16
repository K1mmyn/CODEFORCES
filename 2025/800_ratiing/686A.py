n, k = list(map(int, input().split()))

operations = {
    "-": lambda x, y: x - y,
    "+": lambda x, y: x + y,
}

d = 0

for i in range(n):
    op, a = input().split()
    a = int(a)
    if a > k and op == "-":
        d += 1
    else:
        k = operations[op](k, a)

print(k, d)
