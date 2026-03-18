n, m = list(map(int, input().split(" ")))
seen = set()

for i in range(n):
    list_of_colours = input().split(" ")
    seen.update(list_of_colours)

if "C" in seen or "M" in seen or "Y" in seen:
    print("#Color")
else:
    print("#Black&White")
