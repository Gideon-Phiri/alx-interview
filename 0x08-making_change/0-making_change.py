#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to make the total amount.

    Args:
    coins (list of int): The denominations of coins available.
    total (int): The total amount of money we need to make.

    Returns:
    int: The fewest number of coins needed to make up the total.
         If it's not possible, return -1.
    """
    # Base case: no coins needed if total is zero or less
    if total <= 0:
        return 0

    # Initialize DP array, filled with infinity, and dp[0] = 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop through each amount from 1 to total
    for amount in range(1, total + 1):
        # Check each coin
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, no solution was found
    return dp[total] if dp[total] != float('inf') else -1
