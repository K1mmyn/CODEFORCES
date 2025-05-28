n = int(input())
questions = 0

for x in range(n):
  nums = input()
  nums = nums.split(" ")
  ones_in_nums = 0
  for num in nums:
    if int(num) == 1:
      ones_in_nums += 1

  if ones_in_nums >= 2:
    questions += 1

print(questions)
