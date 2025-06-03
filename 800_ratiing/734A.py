n = int(input())
a = 0 
for char in input():
  if char == "A":
    a += 1
d = n - a

if d == a:
  print("Friendship")
elif d < a:
  print("Anton")
else:
  print("Danik")