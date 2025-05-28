user_input = input()
nums = input()
n, k = user_input.split(" ")
nums = nums.split(" ")
n = int(n)
k = int(k)
count = 0

threshold = int(nums[k - 1])

for num in nums:
  if int(num) >= threshold and int(num) > 0:
    count +=1

print(count)