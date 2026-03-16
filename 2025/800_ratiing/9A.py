from fractions import Fraction

Y, W = list(map(int, input().split()))

maxx = max(Y, W)
chance = 6 - maxx + 1

print(Fraction(chance, 6))
