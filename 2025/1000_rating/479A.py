a = int(input())
b = int(input())
c = int(input())
sums = []

sums.append(a + b + c)
sums.append(a * b * c)
sums.append(a * (b + c))
sums.append((a + b) * c)

print(max(sums))
