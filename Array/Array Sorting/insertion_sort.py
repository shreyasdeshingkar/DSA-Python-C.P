## Implementation
def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

## Driver code 
arr = [50,38,45,79,19,27,29]
## Function calling
result = insertionSort(arr)
print("Sorted array by selection sort is:", result)