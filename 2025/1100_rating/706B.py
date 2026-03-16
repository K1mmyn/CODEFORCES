n = int(input())
prices = list(map(int, input().split(" ")))
prices = sorted(prices)
q = int(input())

def binary_search(sorted_list, target):
  left = 0
  right = len(sorted_list) - 1

  while right >= left:
    middle = (left + right) // 2
    if sorted_list[middle] <= target:
      left = middle + 1
    else:
      right = middle - 1
  return left 

for i in range(q):
  money = int(input())
  print(binary_search(prices, money))

  