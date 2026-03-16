rules = list(map(int, input().split()))
s = [int(x) for x in list(input())]

score = 0

for rule in s:
    score += rules[rule - 1]

print(score)
