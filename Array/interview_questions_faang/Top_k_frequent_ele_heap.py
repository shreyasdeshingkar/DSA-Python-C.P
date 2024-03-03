from collections import Counter
import heapq
def topKfrequentElement(arr,k):
    if k == len(arr):
        return set(arr)
    
    count = Counter(arr)  ## count is dictionary which contains unique values as the key and 
    ## the frequency of those unique elements as the value 
    print(count)
    return heapq.nlargest(k,count.keys(),key=count.get)  ### Returns the n largest elements in an array



##Driver code
arr = [1,1,1,1,2,2,2,3]
k = 2           ##(Top most 'two' frequent elements in an array)

## Function calling
result = topKfrequentElement(arr,k)
print("The top k frequent elements are:",result)