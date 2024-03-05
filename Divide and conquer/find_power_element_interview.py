# Finding of power of an element when n>=1
# Time complexity : O(log n)
## Function definition
def findPowerOfElement(a,n):
     ## small problem
     if n == 0:
          return 1
     
     if n < 0:
          a = 1/a
          n = -n
          c = findPowerOfElement(a,n)
          result = c * c
        
     if n == 1:
          return a
     else:
          
          ## big problem -> Divide and conquer
          mid = n // 2
          ## recursion
          b = findPowerOfElement(a,mid)  ## Only left sides
          result = b * b
          ## even  
          if n % 2 == 0:
               return result
          else:
               return result * a
               
## Driver code
a = 2
n = -4
## Function calling
result = findPowerOfElement(a,n)
print("The power of the given element is:",result)