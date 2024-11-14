def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:  # Check if the target is found
            return mid
        elif arr[mid] < target:  # If the target is larger, search the right half
            low = mid + 1
        else:  # If the target is smaller, search the left half
            high = mid - 1
    
    return -1  # Return -1 if the target is not found

# Example usage
arr = [12, 23, 34, 56, 78, 90]
target = 56
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found.")
