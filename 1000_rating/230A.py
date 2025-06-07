s,n = list(map(int, input().split(" ")))
dragon_list = []
message = "YES"

for i in range(n):
  dragon = list(map(int, input().split(" ")))
  dragon_list.append(dragon)

while len(dragon_list):
  count = 0 
  for dragon in dragon_list:
    if dragon[0] < s:
      count += 1
      s += dragon[1]
      dragon_list.remove(dragon)
  
  if count == 0:
    message = "NO"
    break

print(message)