def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: array with 0 or 1 elements is already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively apply quick sort to the left and right partitions
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Sorted array using Quick Sort:", sorted_arr)
