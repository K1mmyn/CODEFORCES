string = list(input())

for x in range(len(string) -1, -1 ,-1 ):
  if string[x].upper() in "AOYEUI":
    string.pop(x)
  else:
    string[x] = string[x].lower()

print("."+".".join(string))