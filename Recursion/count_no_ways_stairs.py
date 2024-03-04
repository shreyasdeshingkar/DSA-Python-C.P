## Helper Method
def helper(n):
    if n<=1:
        return n
    return countNumberOfWays (n-1) + countNumberOfWays(n-2)

## Function definition
def countNumberOfWays(s):
    return helper(s+1)


## Driver code
n = 3
result = countNumberOfWays(n)
print("No of ways to reach upstairs is",result)