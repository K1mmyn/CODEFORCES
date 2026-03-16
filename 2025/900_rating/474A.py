keys = [
    "q",
    "w",
    "e",
    "r",
    "t",
    "y",
    "u",
    "i",
    "o",
    "p",
    "a",
    "s",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    ";",
    "z",
    "x",
    "c",
    "v",
    "b",
    "n",
    "m",
    ",",
    ".",
    "/",
]

direction = input()
str = list(input())

if direction == "R":
    print("".join(keys[keys.index(str[i]) - 1] for i in range(len(str))))
else:
    print("".join(keys[keys.index(str[i]) + 1] for i in range(len(str))))
