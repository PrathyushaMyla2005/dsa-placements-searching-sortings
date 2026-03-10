'''Bubble Sort Algorithm .
Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.
Example 1:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5'''
def bubble_sort(arr): #function to perform bubble sort
    n = len(arr) #length of the array
    for i in range(n): #traverse through all elements in the array
        for j in range(0, n - i - 1): #traverse through the unsorted elements
            if arr[j] > arr[j + 1]: #if the current element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swap the current element with the next element
    return arr
# Example usage
arr = [5, 4, 3, 2, 1]
print("Original array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
'''tc: O(n^2) where n is the number of elements in the array. This is because we have two nested loops, each running n times.
sc: O(1) because we are sorting the array in place and not using any additional data structures.'''
