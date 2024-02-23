# Function defination
def searchSortedMatrix(matrix,target):
    # no.of rows
    m = len(matrix)
    if m==0:
        return False
    #no.of columns
    n = len(matrix[0])
    
    left ,right = 0,m*n-1

    while left <= right:
        mid = left + (right-left)//2
        ## extractring the elements from the 2D array
        ## row_number = idx(index of element for which we calculating the position) // no.columns(n)
        ## column number = idx(index of element for which we calculating the position) % no.columns(n)
        
        mid_element = matrix[mid//n][mid%n]

        if target == mid_element:
            return True
        
        elif target < mid_element:
            right = mid - 1

        else :
            left = mid + 1
    return False
        







## Driver code
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# Function call
result = searchSortedMatrix(matrix,target)
print(result)