str = input()
found = set()

for char in str:
    if char.isalpha() and char not in found:
        found.add(char)

print(len(found))
