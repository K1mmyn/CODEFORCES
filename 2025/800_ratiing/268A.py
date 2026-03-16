n = int(input())

teams = []

for i in range(n):
    teams.append(input().split())

count = 0

for i in range(n):
    for j in range(n):
        if j == i:
            continue
        if teams[i][0] == teams[j][1]:
            count += 1

print(count)
