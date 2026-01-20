a = [3, 5, 35, 3, 2, 5, 33, 44]
k = 3

window_sum = sum(a[:k])
max_sum = window_sum

for i in range(k, len(a)):
    window_sum += a[i]        # add next element
    window_sum -= a[i - k]    # remove left element
    max_sum = max(max_sum, window_sum)

print(f"max is {max_sum}")
