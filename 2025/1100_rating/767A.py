n = int(input())
snacks = list(map(int, input().split()))
present = [False] * n

for i in range(n):
    present[snacks[i] - 1] = True

    while n >= 1 and present[n - 1]:
        print(n, end=" ")
        n -= 1

    print()
