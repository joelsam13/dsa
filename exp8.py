def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Element to be positioned
        j = i - 1
        # Shift elements of the sorted portion that are greater than the key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place key in its correct position

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array using Insertion Sort:", arr)
