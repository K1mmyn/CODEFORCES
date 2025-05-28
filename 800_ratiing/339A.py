nums = list(map(int, input().split("+")))

for x in range(len(nums)):
  swap = 0 
  for y in range(1 + x,len(nums)):
    if nums[x] > nums[y]:
      nums[x], nums[y] = nums[y], nums[x]
      swap += 1

print('+'.join(list(map(str,nums))))