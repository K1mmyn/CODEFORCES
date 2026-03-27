t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    count = 0
    maxx = max(nums)

    for num in nums:
        if num == maxx:
            count += 1

    print(count)
