s = input()
t = input()

if s == ''.join(t[::-1]):
  print("YES")
else:
  print("NO")