## function defination
## Approach 1: Using slope concept
## Time complexity and Space complexity: O(1)


# def iscollinearPoints(x1,x2,x3,y1,y2,y3):
#     if((y2-y1)*(x3-x2) == (y3-y2)*(x2-x1)): ## cross multiplication of the slope fromula of three points formula
#         print("Yes,the given points are collinear")
#     else:
#         print("No,the given points are not collinear")

# ## Driver code 
# x1,x2,x3,y1,y2,y3 = 1,2,3,6,0,9
# iscollinearPoints(x1,x2,x3,y1,y2,y3)



## Approach 2: Using area of traingle
## Time complexity and Space complexity: O(1)


def iscollinearPoints(x1,x2,x3,y1,y2,y3):
    area = 0.5 * (x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))
    if area == 0:
        print("Yes,the given points are collinear")
    else:
        print("No,the given points are not collinear")


## Driver code 
x1,x2,x3,y1,y2,y3 = 1,1,1,6,0,9
iscollinearPoints(x1,x2,x3,y1,y2,y3)