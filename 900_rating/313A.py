n = int(input())

if n > 0:
  print(n)
else:
  n = list(str(n))

  x = ''.join(num for num in n[:-1])
  y = ''.join(num for num in n[:-2])
  y += n[-1]
  if x < y:
    print(int(x))
  else:
    print(int(y))