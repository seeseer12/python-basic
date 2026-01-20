a = [3, 5, 35, 3, 2, 5, 33, 44]
max_sum = 0

for i in range(len(a) - 2):
    added = 0
    for j in range(i, i + 3):
        added += a[j]
    max_sum = max(max_sum, added)

print(f"max is {max_sum}")
