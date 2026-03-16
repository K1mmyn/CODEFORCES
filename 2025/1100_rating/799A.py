import math

n, t, k, d = list(map(int, input().split()))

totalTime = t * math.ceil(n / k)
bread_made_before_time_d = (d // t) * k
secondTime = d + (t * math.ceil((n - bread_made_before_time_d) / (k * 2)))

print(totalTime, secondTime)

if totalTime > secondTime:

    print("YES")
else:
    print("NO")
