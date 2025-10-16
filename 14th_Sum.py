def maxProfit(prices):
    # Initialize the minimum price and maximum profit
    min_val = prices[0]   # lowest price seen so far (best buy)
    profit = 0            # maximum profit so far

    # Loop through the prices starting from the second day
    for i in range(1, len(prices)):
        cost = prices[i] - min_val       # profit if sold today
        profit = max(profit, cost)       # update max profit
        min_val = min(min_val, prices[i]) # update min price (best buying price)

    # Return the highest profit after checking all days
    return profit
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
