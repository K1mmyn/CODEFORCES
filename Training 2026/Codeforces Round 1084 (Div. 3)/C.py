t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    stack = []

    for i in range(n):
        char = s[i]

        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print("YES" if not stack else "NO")
