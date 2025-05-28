nums = list(input())
output = "YES"
count = 0

for num in nums:
  if (num == "4" or num == "7"):
    count += 1

if count != 4 and count != 7:
   output = "NO"

print(output)