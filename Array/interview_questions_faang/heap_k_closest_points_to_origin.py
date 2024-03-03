## time complexity: 
from heapq import heappush,heappop
import math
## get_dist is to give the euclidean distance
def get_dist(x,y):
    return math.sqrt(x**2 + y**2)


def kClosestPoints(points, k):
    min_heap = []
    n = len(points)
    for i in range(n):
        x = points[i][0]
        y = points[i][1]

        ## to insert the elements inside the minheap
        heappush(min_heap, (get_dist(x,y),points[i]))

    result = []
    for i in range(k):
        ## to delete the elements from the minheap
        result.append(heappop(min_heap)[1])   ## [1] is written here since we want to displayonly points[i] from min_heap not the distances..

    return result



## Driver Code
points = [[3,3],[5,-1],[-2,4]]
k = 2
## Function calling
result = kClosestPoints(points, k)
print ("The k closest points to the origin are:",result)