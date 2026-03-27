t = int(input())


def sort_by_rotation(nums):
    return nums[nums.index(min(nums)) :] + nums[: nums.index(min(nums))]


for _ in range(t):
    n, startP, endP = list(map(int, input().split(" ")))

    nums = list(map(int, input().split(" ")))
    outside = nums[:startP] + nums[endP:]
    inside = sort_by_rotation(nums[startP:endP])

    if not outside:
        print(*inside)
        continue

    flag = False
    for i in range(len(outside)):
        if outside[i] > inside[0]:
            print(*(outside[:i] + inside + outside[i:]))
            flag = True
            break

    if not flag:
        print(*(outside + inside))
