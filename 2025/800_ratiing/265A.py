s = input()
t = input()

point = 0

for i in range(len(t)):
    if s[point] == t[i]:
        point += 1

print(point + 1)
