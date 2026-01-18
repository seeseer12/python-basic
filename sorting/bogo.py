import random

def is_sorted(arr):
    """Check if array is sorted in ascending order"""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    """Bogo Sort - randomly shuffles array until it's sorted"""
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    return arr, attempts

if __name__ == "__main__":
    numbers = [5, 2, 8, 1, 9, 3]
    print(f"Original: {numbers}")
    sorted_numbers, tries = bogo_sort(numbers.copy())
    print(f"Sorted: {sorted_numbers} in {tries} attempts")
