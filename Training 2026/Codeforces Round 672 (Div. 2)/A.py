import sys


def solve():
    input_data = sys.stdin.read().split()

    it = iter(input_data)
    t = int(next(it))
    for _ in range(t):
        n = int(next(it))
        nums = [int(next(it)) for _ in range(n)]

        maxx_inversion = ((n * (n - 1)) / 2) - 1

        possible = False

        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                possible = True
                break

        sys.stdout.write("YES\n" if possible else "NO\n")


if __name__ == "__main__":
    solve()
