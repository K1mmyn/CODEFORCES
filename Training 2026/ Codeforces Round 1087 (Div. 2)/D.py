import heapq
import collections

n = int(input())
f = []

for _ in range(n):
    R, G, B = map(int, input().split(" "))

    keys = ["R", "G", "B"]
    counter = {"R": R, "G": G, "B": B}
    states = {"R": True, "G": True, "B": True, "": False}

    for key in keys:
        if counter[key] == 0:
            states[key] = False

    prev = collections.deque(["", "", ""])

    text = ""

    while states["R"] or states["B"] or states["G"]:
        usable = {key for key in keys if states[key]}
        toUse = max(usable, key=lambda k: (counter[k], prev[1] == k))

        text += toUse
        counter[toUse] -= 1

        prev.popleft()
        prev.append(toUse)

        states = {"R": True, "G": True, "B": True, "": False}

        states[prev[0]] = False
        states[prev[1]] = True
        states[prev[2]] = False

        for key in keys:
            if counter[key] == 0:
                states[key] = False

    f.append(text)

print("\n".join(f) + "\n")
