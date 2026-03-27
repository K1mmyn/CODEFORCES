t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    index = 0

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            index += 1
            break

    if index:
        print(1)
    else:
        print(n)
