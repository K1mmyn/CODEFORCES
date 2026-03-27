import math


def primeFactorization(n):
    factors = set()

    while n % 2 == 0:
        factors.add(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i

    if n > 2:
        factors.add(n)

    if len(factors) > 1:
        return -1

    if len(factors) == 0:
        return 1

    return factors.pop()


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    is_sorted = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            is_sorted = False
            break

    if is_sorted:
        print("Bob")
        continue

    is_sorted = True

    factors = []
    flag = False
    for element in a:
        res = primeFactorization(element)
        if res == -1:
            flag = True
            break
        factors.append(res)

    if flag:
        print("Alice")
        continue

    for i in range(len(factors) - 1):
        if factors[i] > factors[i + 1]:
            is_sorted = False
            break

    if is_sorted:
        print("Bob")
    else:
        print("Alice")
