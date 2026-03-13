# Function to rearrange the array and place pivot at correct position
def partition(arr, low, high):
    
    # Select the last element of the array as the pivot
    pivot = arr[high]

    # 'i' will keep track of the index of smaller elements
    # We start from one position before 'low'
    i = low - 1

    # Loop through the array from index 'low' to 'high-1'
    # 'j' is used to check each element
    for j in range(low, high):

        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:

            # Move 'i' one step forward
            i = i + 1

            # Swap the smaller element with the element at index 'i'
            # This moves smaller elements to the left side
            arr[i], arr[j] = arr[j], arr[i]

    # After the loop, place the pivot element in its correct sorted position
    # Swap pivot with the element next to 'i'
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the index where pivot is placed
    return i + 1


# Function to perform Quick Sort
def quickSort(arr, low, high):

    # Continue sorting only if there is more than one element
    if low < high:

        # Partition the array and get pivot position
        pi = partition(arr, low, high)

        # Recursively sort the left part of the pivot
        # Elements before pivot
        quickSort(arr, low, pi - 1)

        # Recursively sort the right part of the pivot
        # Elements after pivot
        quickSort(arr, pi + 1, high)


# Given array to be sorted
arr = [10, 7, 8, 9, 1, 5]

# Call quickSort function
# '0' is starting index
# 'len(arr)-1' is last index
quickSort(arr, 0, len(arr) - 1)

# Print the sorted array
print(arr)