import sys


def solve():
    input_data = sys.stdin.read().split()

    it = iter(input_data)
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    nums_sort = nums.copy()
    nums_sort.sort()

    pref_n = [0] * (n + 1)
    pref_s = [0] * (n + 1)

    for i in range(n):
        pref_n[i + 1] = pref_n[i] + nums[i]
        pref_s[i + 1] = pref_s[i] + nums_sort[i]

    t = int(next(it))

    for _ in range(t):
        type = int(next(it))
        l = int(next(it))
        r = int(next(it))

        if type == 1:
            print(pref_n[r] - pref_n[l - 1])
        else:
            print(pref_s[r] - pref_s[l - 1])


if __name__ == "__main__":
    solve()
