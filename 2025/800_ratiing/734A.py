import math

n = int(input())
string = input()

a_count = sum(1 for char in string if char == "A")

if a_count == len(string) / 2:
    print("Friendship")
elif a_count > len(string) / 2:
    print("Anton")
else:
    print("Danik")
