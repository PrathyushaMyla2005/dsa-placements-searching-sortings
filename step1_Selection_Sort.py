'''Selection Sort Algorithm
Problem Statement: Given an array of N integers, 
write a program to implement the Selection sorting algorithm.
Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52'''
def selection_sort(arr): #function to perform selection sort
    n = len(arr) #length of the array
    for i in range(n - 1): #traverse through all elements in the array
        min_index = i #initialize the minimum index to the current index
        for j in range(i + 1, n): #traverse through the unsorted elements
            if arr[j] < arr[min_index]: #if the current element is smaller than the minimum element
                min_index = j #update the minimum index
        arr[i], arr[min_index] = arr[min_index], arr[i] #swap the minimum element with the current element
    return arr
# Example usage
arr = [13, 46, 24, 52, 20, 9]
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
'''tc: O(n^2) where n is the number of elements in the array. This is because we have two nested loops, each running n times.
sc: O(1) because we are sorting the array in place and not using any additional data structures.'''