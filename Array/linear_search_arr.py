
## Q. Search for an element '15' if its present in an array ,return the index of that element
## Suppose the searching element is not present in an array return -1

## Time complexity :O(n)
## Space complexity :O(1)
def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1



## Driver code 
arr = [2,1,8,4,7,9,12,15,11,19]
x = 15
##Function calling
result = linearSearch(arr,x)
print("Searching element is present at the index",result)

