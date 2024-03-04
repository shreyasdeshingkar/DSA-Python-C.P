## Function definition
def fibonacciSeries(n):
    ## Base case condition
    if n <= 1:
        return n
    else:
        return fibonacciSeries(n-1) + fibonacciSeries(n-2)


## Driver code 
n = 10
for i in range(n):
    print(fibonacciSeries(i))

