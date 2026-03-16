from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
first = min(nums)
last = max(nums)
counts = Counter(nums)
nums = set(nums)

if len(nums) - 2 <= 0:
    print(0)
else:
    print(n - counts[first] - counts[last])
