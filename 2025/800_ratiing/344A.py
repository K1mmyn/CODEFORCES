n = int(input())
end = None
groups = 0

for i in range(n):
    mag = input()
    if i == 0:
        end = mag
        groups += 1
        continue

    if mag != end:
        groups += 1
        end = mag

print(groups)
