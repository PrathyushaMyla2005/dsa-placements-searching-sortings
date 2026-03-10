'''Insertion Sort Algorithm
Problem Statement: Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.'''
def insertion_sort(nums):# function to perform insertion sort
    for i in range(1,len(nums)): #loop through the array starting from the second elemeent
        key = nums[i] #store the current element as key
        j = i-1 #initialize j to be the index of the last sorted element
        while j>=0 and nums[j]>key: #loop through the sorted elements and shift them to the right until we find the correct position for the key
            nums[j+1] = nums[j] #shift the element to the right
            j -= 1 #decrement j to check the next element
        nums[j+1] = key #insert the key at its correct position in the sorted array
    return nums #return the sorted array
# Example usage
nums = [12, 11, 13, 5, 6]
sorted_nums = insertion_sort(nums)
print("Sorted array is:", sorted_nums)
'''tc: O(n^2) in the worst case when the array is sorted in reverse order, O(n) in the best case when the array is already sorted, and O(n^2) on average. sc: O(1) because we are sorting the array in place without using any additional data structures.
Insertion sort is a simple and efficient algorithm for sorting small datasets. It works by dividing the array into a sorted and an unsorted part, and iteratively inserting elements from the unsorted part into the correct position in the sorted part. The algorithm is stable, meaning that it preserves the relative order of equal elements. However, it is not suitable for large datasets due to its quadratic time complexity.
Insertion sort is often used as a building block in more complex sorting algorithms, such as Timsort, which is used in Python's built-in sorting functions. It is also useful for sorting small arrays or partially sorted arrays, where it can perform better than more complex algorithms.'''