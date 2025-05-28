string = list(input())
dangerous = "NO"
count = 0

for x in range(len(string) -1):
  if string[x] == string[x + 1]:
    count += 1
  if count == 6:
    dangerous = "YES"
    break
  if string[x] != string[x + 1]:
    count = 0

print(dangerous)
