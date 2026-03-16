import random

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

n, k = list(map(int, input().split()))

sample = random.sample(alphabet, k)

for i in range(n - k):
    char = sample[i % k]
    if char == sample[-1]:
        char = sample[(i + 1) % k]
    sample.append(char)

print("".join(sample))
