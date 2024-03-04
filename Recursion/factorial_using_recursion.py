## Using recursion
## Time complexity:O(n)
## Function definition
# def findFactorial(n):
#     # Base case condition
#     if n==0 or n==1:
#         return 1
#     else:
#         ## Big problem
#         ## Recursion
#         return n * findFactorial(n-1)


# ## Driver code
# n = 8
# ## Function calling
# result = findFactorial(n)
# print("The factorial of a given number is:",result)







## Using iterative method
## Time complexity:O(n)
## Function definition
def findFactorial(n):
    fact = 1
    # Base case condition
    if n==0 or n==1:
        return 1
    else:
        ## iterative approach
        for i in range(2,n+1):
            fact = fact * i
        return fact


## Driver code
n = 8
## Function calling
result = findFactorial(n)
print("The factorial of a given number is:",result)