#Implementation
# Recurrance relation : T(n) = t(n/3) + c
# Function definition
def ternary_search(l,r,arr,key):
    while l<=r:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3

        if key == arr[mid1]:
            return mid1
        elif key == arr[mid2]:
            return mid2
        # First search space 
        elif key < arr[mid1]:
            r = mid1 - 1
        # Third search space
        elif key >arr[mid2]:
            l = mid2 + 1
        #Second search space
        else:
            l=mid1+1
            r=mid2-1
    return -1






# Driver code
arr = [3,10,15,20,25,29,35,40]
l = 0
r = len(arr) - 1
key = 2
# Function calling
result = ternary_search(l,r,arr, key)
print("Searching element is present at index",result)