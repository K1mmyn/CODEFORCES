# nums = list(map(int, input().split("+")))

# for x in range(len(nums)):
#   swap = 0
#   for y in range(1 + x,len(nums)):
#     if nums[x] > nums[y]:
#       nums[x], nums[y] = nums[y], nums[x]
#       swap += 1

# print('+'.join(list(map(str,nums))))

# * Optimised solution O(n)

s = input().split("+")
ones = s.count("1")
twos = s.count("2")
threes = s.count("3")
result = ["1"] * ones + (["2"] * twos) + (["3"] * threes)
print("+".join(result))
