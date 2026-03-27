import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    t = int(next(it))

    final_output = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]

        res = [0] * n
        for i in range(n):
            target = a[i]
            less = 0
            more = 0
            for j in range(i + 1, n):
                val = a[j]
                if val < target:
                    less += 1
                elif val > target:
                    more += 1

            res[i] = less if less > more else more

        final_output.append(" ".join(map(str, res)))

    sys.stdout.write("\n".join(final_output) + "\n")


if __name__ == "__main__":
    solve()
