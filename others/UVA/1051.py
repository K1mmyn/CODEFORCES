n = int(input())
for i in range(n):
    if i == 0:
        print("no")
        continue

    num = int(input())
    if num % i == 0:
        print("yes")
    else:
        print("no")
