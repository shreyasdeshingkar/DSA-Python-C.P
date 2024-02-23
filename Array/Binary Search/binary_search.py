# Time Complexity: O(logn)
## Implementation of Binary Search using recursion
# def BinarySearch(arr,i,j,key):
#     while i<=j:
#         mid = i + (j-i)//2

#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             ## Recursion-> Calling the same function again with different set of parameters
#             return BinarySearch(arr,mid+1,j,key)
#         else:
#             return BinarySearch(arr,i,mid-1,key)
    
#     ##Searching element is not present in an array
#     return -1

# ## Driver Code
# ## Sorted array
# arr = [2,4,5,8,28,45,56,67,78,89]
# key = 67
# i = 0
# j = len(arr)-1

# #Function Call
# result = BinarySearch(arr, i, j, key)
# print("Searching element is present at index:",result)









## Implementation of Binary Search without using recursion 
def BinarySearch(arr,i,j,key):
    while i<=j:
        mid = i + (j-i)//2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            #Update the i parameter
            i = mid + 1
        else:
            #Update the j parameter
            j = mid - 1
            
    
    ##Searching element is not present in an array
    return -1

## Driver Code
## Sorted array
arr = [2,4,5,8,28,45,56,67,78,89]
key = 67
i = 0
j = len(arr)-1

#Function Call
result = BinarySearch(arr, i, j, key)
print("Searching element is present at index:",result)