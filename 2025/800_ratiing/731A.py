s = input()

letters_mod26 = {
    "a": [0, 0],
    "b": [1, -25],
    "c": [2, -24],
    "d": [3, -23],
    "e": [4, -22],
    "f": [5, -21],
    "g": [6, -20],
    "h": [7, -19],
    "i": [8, -18],
    "j": [9, -17],
    "k": [10, -16],
    "l": [11, -15],
    "m": [12, -14],
    "n": [13, -13],
    "o": [14, -12],
    "p": [15, -11],
    "q": [16, -10],
    "r": [17, -9],
    "s": [18, -8],
    "t": [19, -7],
    "u": [20, -6],
    "v": [21, -5],
    "w": [22, -4],
    "x": [23, -3],
    "y": [24, -2],
    "z": [25, -1],
}

count = 0

for char in s:
    add = min(
        abs(letters_mod26[current][1] - letters_mod26[char][0]) % 26,
        abs(letters_mod26[current][0] - letters_mod26[char][1]) % 26,
    )
    count += add
    current = char

print(count)
