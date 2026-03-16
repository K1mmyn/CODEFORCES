n = int(input())
nums = list(map(int, input().split()))

l = 0
r = len(nums) - 1
s = 0
d = 0


for turn in range(n):
    if nums[l] > nums[r]:
        if turn % 2 == 0:
            s += nums[l]
        else:
            d += nums[l]
        l += 1
    else:
        if turn % 2 == 0:
            s += nums[r]
        else:
            d += nums[r]
        r -= 1

print(s, d)
