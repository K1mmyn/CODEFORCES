row_pos = None
col_pos = None

for i in range(5):
    nums = input().split()

    for k in range(5):
        if nums[k] == "1":
            row_pos = k
            col_pos = i
            break

print(abs(row_pos - 2) + abs(col_pos - 2))
