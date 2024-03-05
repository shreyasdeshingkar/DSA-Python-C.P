## Divide and Conquer Approach
## Time Complexity: O(n)
## function definition
def findMaxandMin(arr,i,j):
    ## Small problem
    ## single element in an array
    if i == j:
        min_val = arr[i]
        max_val = arr[i]
    
    ## Two elements in an array
    elif i == j - 1:
        if arr[i] < arr[j]:
            min_val = arr[i]
            max_val = arr[j]
        else:
            min_val = arr[j]
            max_val = arr[i]
    
    ## big problem -> Divide and conquer approach
    else:
        ## Divide
        mid = i + (j-i)//2
        
        ## Recursion -> Conqur
        max_l,min_l = findMaxandMin(arr, i, mid)        
        max_r,min_r = findMaxandMin(arr, mid+1, j)
        
        ##  Combine results
        ## to find the final max_val
        if max_l < max_r:
            max_val = max_r
        else:
            max_val = max_l

        ## to find the final min_val
        if min_l < min_r:
            min_val = min_l
        else:
            min_val = min_r

    return max_val,min_val

## Driver code
arr = [70,50,45,10,12,15,75,10000,-2]
i = 0
j = len(arr)- 1

## function calling
max_val,min_val = findMaxandMin(arr,i,j)
print("The maximum and minimum value in the array is :", max_val,min_val)