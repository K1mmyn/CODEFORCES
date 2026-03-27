import sys


def solve():

    input_data = sys.stdin.read().split()

    it = iter(input_data)
    chars = list(next(it))
    chars_pref = [0] * len(chars)
    for i in range(len(chars) - 1):

        is_good = 1 if chars[i] == chars[i + 1] else 0

        chars_pref[i + 1] = chars_pref[i] + is_good

    m = int(next(it))

    for _ in range(m):
        l = int(next(it))
        r = int(next(it))
        print(chars_pref[r - 1] - chars_pref[l - 1])


if __name__ == "__main__":
    solve()
