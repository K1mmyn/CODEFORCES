n, k = list(map(int, input().split()))
s = input()


def helper(char):
    l = 0
    changes = 0
    longest_sub = 0

    for r in range(len(s)):
        if s[r] != char:
            changes += 1

        while changes > k:
            if s[l] != char:
                changes -= 1
            l += 1

        longest_sub = max(longest_sub, r - l + 1)

    return longest_sub


print(max(helper("a"), helper("b")))
