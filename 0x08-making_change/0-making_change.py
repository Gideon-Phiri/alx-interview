#!/usr/bin/python3
"""
This module contains a function to determine the fewest number of coins
required to make a given amount using a dynamic programming approach.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
    coins (list of int): List of the denominations of coins.
    total (int): The total amount to meet.

    Returns:
    int: The minimum number of coins to meet the total, or -1 if impossible.
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
