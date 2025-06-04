numbers = list(input())
number = int(''.join(numbers))
valid = True

def is_multiple(num, divisor, lucky_num, alternate=True):
  while divisor < num:
    if number % divisor == 0:
      return True
    
    divisor *= 10
    if alternate:
      if list(divisor)[0] == 4:
        divisor += 7
      else:
        divisor += 4
    else:
      divisor += lucky_num

  return False

for num in numbers:
  if num != "4" and num != "7":
    valid = False

if valid:
  print("YES")
else:
  multiple1 = is_multiple(number, 4, 4, alternate=False)
  multiple2 = is_multiple(number, 7, 7, alternate=False)
  multiple3 = is_multiple(number, 4, 7, alternate=False)
  multiple4 = is_multiple(number, 7, 4, alternate=False)
  if multiple1 or multiple2 or multiple3 or multiple4:
    print("YES")
  else:
    print("NO")