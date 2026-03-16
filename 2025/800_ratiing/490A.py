n = int(input())
children = input().split()

freq = {
    "1": [],
    "2": [],
    "3": [],
}

teams = 0

for i in range(len(children)):
    skill = children[i]
    freq[skill].append(i + 1)

teams = min(len(freq[i]) for i in freq.keys())

print(teams)
for i in range(teams):
    for j in range(1, 4):
        print(freq[f"{j}"].pop(), end=" ")
    print()
