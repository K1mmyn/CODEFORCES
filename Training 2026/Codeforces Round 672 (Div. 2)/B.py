t = int(input())

for _ in range(t):
    n = int(input())
    nums = [int(i).bit_length() for i in input().split(" ")]
    count = 0
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for val in freq.values():
        count += (val * (val - 1)) // 2

    print(count)
