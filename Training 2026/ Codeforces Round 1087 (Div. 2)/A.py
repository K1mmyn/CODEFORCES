t = int(input())

for _ in range(t):
    n, c, k = list(map(int, input().split(" ")))
    nums = list(map(int, input().split(" ")))
    nums.sort()

    for num in nums:
        if num > c:
            break

        diff = abs(num - c)
        amount = min(diff, k)
        c += num + amount
        k -= amount

    print(c)
