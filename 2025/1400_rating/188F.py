import math

num = int(input())
binary_str = ""

for i in range(math.ceil(math.log2(num)) - 1, -1, -1):
    if num // 2 == num / 2:
        binary_str = "0" + binary_str
    else:
        binary_str = "1" + binary_str
    num //= 2
#
print(binary_str)
