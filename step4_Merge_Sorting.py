'''Merge Sort Algorithm
Problem Statement: Given an array of size n, sort the array using Merge Sort.'''
# Function to merge two sorted halves of the array
def merge(arr, low, mid, high):

    temp = []              # Temporary list to store merged sorted elements

    left = low             # Starting index of the left half
    right = mid + 1        # Starting index of the right half


    # Compare elements from both halves and store the smaller one in temp
    while left <= mid and right <= high:

        # If left element is smaller or equal
        if arr[left] <= arr[right]:

            temp.append(arr[left])   # Add left element to temp
            left += 1                # Move left pointer to next element

        else:

            temp.append(arr[right])  # Add right element to temp
            right += 1               # Move right pointer to next element


    # If elements remain in the left half, add them to temp
    while left <= mid:

        temp.append(arr[left])   # Add remaining left element
        left += 1                # Move pointer


    # If elements remain in the right half, add them to temp
    while right <= high:

        temp.append(arr[right])  # Add remaining right element
        right += 1               # Move pointer


    # Copy the sorted elements from temp back into the original array
    for i in range(low, high + 1):

        arr[i] = temp[i - low]   # Place elements in correct positions in arr



# Recursive function that divides the array
def mergeSort(arr, low, high):

    # Base condition: if only one element, already sorted
    if low >= high:
        return


    mid = (low + high) // 2      # Find the middle index


    # Recursively sort the left half
    mergeSort(arr, low, mid)


    # Recursively sort the right half
    mergeSort(arr, mid + 1, high)


    # Merge the two sorted halves
    merge(arr, low, mid, high)



# Driver Code (main program)

arr = [5, 2, 8, 4, 1]     # Unsorted array

mergeSort(arr, 0, len(arr) - 1)   # Call merge sort on the whole array

print(arr)                # Print the sorted array
'''Time Complexity: O(N*logN), merging two arrays take linear time and array is recursively divided into halves (logN times).
Space Complexity: O(N), we use a temporary array to store elements in sorted order.
'''