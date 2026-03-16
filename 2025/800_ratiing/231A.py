n = int(input())
questions = 0

for x in range(n):
    nums = list(map(int, input().split()))
    if sum(nums) > 1:
        questions += 1

print(questions)
