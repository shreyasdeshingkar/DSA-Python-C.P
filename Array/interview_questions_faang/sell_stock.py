## Implementation
## Time complexity: O(n)
## Space complexity: O(1)
def findmaxProfit(prices):
    n = len(prices)
    min_price = float('inf')
    max_profit = 0

    for i in range(n):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit


## Driver code
prices = [7,1,5,3,6,4,15]
## Function calling
maxProfit = findmaxProfit(prices)
print("The maximum profit of buy and sell the stock is:",maxProfit)