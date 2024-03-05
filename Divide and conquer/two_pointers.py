## Function definition
## Time complexity : O(n)
def twoPointerSum(arr,target):
    l = 0
    r = len(arr)-1
    for i in range(len(arr)-1):
        if arr[l] + arr[r] == target:
            return l,r
        
        elif arr[l] + arr[r] > target:
            r = r - 1
        else:
            l = l + 1
    return -1,-1

## Driver code
arr = [20,40,50,75,120,145,200]
target = 60

result = twoPointerSum(arr,target)
print(result)