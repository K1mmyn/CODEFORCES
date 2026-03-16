from collections import Counter

n = int(input())
counts = Counter(input().lower())

if len(counts.keys()) == 26:
    print("YES")
else:
    print("NO")
