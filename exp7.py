def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the minimum is the first element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Find the actual minimum
                min_index = j
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array using Selection Sort:", arr)
