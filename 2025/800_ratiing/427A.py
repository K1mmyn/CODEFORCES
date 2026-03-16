n = int(input())
crimes = list(map(int, input().split()))

police = 0
count = 0

for crime in crimes:
    if crime < 0:
        if police == 0:
            count -= crime
        else:
            police -= 1
    else:
        police += crime

print(count)
