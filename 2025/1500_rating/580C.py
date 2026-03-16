import sys

sys.setrecursionlimit(200000)

n, m = list(map(int, input().split()))
catdata = list(map(int, input().split()))
freq = {i: [] for i in range(1, n + 1)}

for i in range(n - 1):
    parent, node = list(map(int, input().split()))
    freq[parent].append(node)
    freq[node].append(parent)

restaurants = 0


def dfs(node, parent, streak):
    global restaurants
    if catdata[node - 1] == 1:
        streak += 1
    else:
        streak = 0

    if streak > m:
        return

    if len(freq[node]) == 1 and node != 1:
        restaurants += 1

    for i in freq[node]:
        if i != parent:
            dfs(i, node, streak)

    return


dfs(1, -1, 0)

print(restaurants)
