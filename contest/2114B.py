s = int(input())

for i in range(s):
  n,k = list(map(int, input().split(" ")))
  b_string = list(input())
  pairs = 0
  n = n // 2

  for i in range(1, n + 1):
    print((n*2) - i, i -1 )
    if b_string[(n * 2)-i] == b_string[i - 1]:
      pairs += 1

  rearrange = n - pairs

  if pairs == k:
    print('YES')
  else:
    print('NO')
