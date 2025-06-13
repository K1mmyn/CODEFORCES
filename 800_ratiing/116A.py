n = int(input())
onboard = [0]

for i in range(n):
  a,b = list(map(int, input().split(" ")))
  onboard.append(onboard[-1] - a + b)

print(max(onboard))
