n, m = list(map(int, input().split(" ")))
tasks = list(map(int, input().split(" ")))
count = 0
current = 1

for task in tasks:

  if task < current:
    count += (n - current) + task
    current = task
  else:
    count += (task - current) 
    current = task

print(count)