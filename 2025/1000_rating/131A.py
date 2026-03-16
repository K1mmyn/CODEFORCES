string = list(input())
count_lower = 0
index = None

for x in range(len(string)):
  if string[x].lower() == string[x]:
    count_lower += 1
    index = x

if (count_lower == 1 and string[0] == string[0].lower()) or count_lower == 0:
  for x in range(len(string)):
    if string[x].upper() == string[x]:
      string[x] = string[x].lower()
    else:
      string[x] = string[x].upper()

print("".join(string))
