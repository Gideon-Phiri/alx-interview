#!/usr/bin/python3
"""
Main file for testing the makeChange function.
"""


makeChange = __import__('0-making_change').makeChange

# Test case 1: Small total, possible
print(makeChange([1, 2, 25], 5))  # Expected output: 3

# Test case 2: Small total, impossible
print(makeChange([3], 2))  # Expected output: -1

# Test case 3: Large total, possible
print(makeChange([1, 5, 10, 25], 1000))  # Expected output: 40

# Test case 4: Large total, impossible
print(makeChange([2, 4], 7))  # Expected output: -1

# Test case 5: Negative total
print(makeChange([1, 2, 5], -5))  # Expected output: 0

# Test case 6: Zero total
print(makeChange([1, 2, 5], 0))  # Expected output: 0

# Test case 7: Normal coins
print(makeChange([1, 2, 5, 10], 18))  # Expected output: 5

# Test case 8: No coins
print(makeChange([], 10))  # Expected output: -1

# Test case 9: Long list of coins
print(makeChange([1, 2, 5, 10, 25, 50, 100, 200], 1000))  # Expected output: 10

# Test case 10: Runtime check - possible total
print(makeChange([1, 5, 10], 1000000))  # Expected output: large value (around 100000)

# Test case 11: Runtime check - impossible total
print(makeChange([2, 3], 999999))  # Expected output: -1
