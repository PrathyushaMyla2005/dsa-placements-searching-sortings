def bubble_sort(arr, n):
    # Base case: if only 1 element, return
    if n == 1:
        return

    # Perform one pass to push the largest to the end
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            # Swap elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Recurse for the rest of the array
    bubble_sort(arr, n - 1)


# Main driver
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

print("Before Using Bubble Sort:")
print(arr)

bubble_sort(arr, n)

print("After Using Bubble Sort:")
print(arr)
