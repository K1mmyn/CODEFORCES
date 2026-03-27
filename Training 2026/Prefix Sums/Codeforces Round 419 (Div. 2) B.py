import sys


def solve():
    input_data = sys.stdin.read().split()

    it = iter(input_data)
    n = int(input_data[0])
    k = int(input_data[1])
    q = int(input_data[2])

    MAX_N = 200005

    freq = [0] * MAX_N
    pref = [0] * MAX_N
    idx = 3

    for _ in range(n):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        freq[l] += 1
        freq[r + 1] -= 1

    curr = 0

    for i in range(1, MAX_N):
        curr += freq[i]

        is_good = 1 if curr >= k else 0
        pref[i] = pref[i - 1] + is_good

    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        print(pref[r] - pref[l - 1])


if __name__ == "__main__":
    solve()
