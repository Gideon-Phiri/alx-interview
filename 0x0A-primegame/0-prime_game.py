#!/usr/bin/python3
"""
Prime Game Algorithm Module
Maria and Ben take turns picking prime numbers and their multiples
from a set of consecutive integers, starting at 1.
The player that cannot make a move loses.
"""


def isWinner(x, nums):
    """
    Determines the winner after x rounds of the prime game.

    Args:
        x: Number of rounds.
        nums: List of n values for each round.

    Returns:
        Name of the player with the most wins, or None if there is a tie.
    """
    if not nums or x < 1:
        return None

    # Get the maximum value from nums to generate primes
    max_n = max(nums)

    # Step 1: Precompute primes up to max_n using Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_n)

    # Initialize win counters
    maria_wins = 0
    ben_wins = 0

    # Step 2: Simulate the game for each value of n in nums
    for n in nums:
        winner = simulate_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 3: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(limit):
    """
    Uses the Sieve of Eratosthenes algorithm to identify all primes <= limit.

    Args:
        limit: The upper boundary of the sieve.

    Returns:
        A list of booleans where True means the index is a prime number.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False

    return is_prime


def simulate_game(n, primes):
    """
    Simulates a single round of the prime game.

    Args:
        n: The upper boundary of the current round.
        primes: Precomputed list of primes.

    Returns:
        The winner of the round: "Maria" or "Ben".
    """
    # Track remaining numbers (True means the number is still available)
    remaining_numbers = [True] * (n + 1)

    current_player = "Maria"  # Maria always starts

    while True:
        move_made = False

        # Look for the next available prime
        for i in range(2, n + 1):
            if remaining_numbers[i] and primes[i]:
                # Remove the prime and all its multiples
                for multiple in range(i, n + 1, i):
                    remaining_numbers[multiple] = False
                move_made = True
                break

        if not move_made:
            # No valid move left; current player loses
            if current_player == "Maria":
                return "Ben"
            else:
                return "Maria"

        # Switch players after a move
        current_player = "Ben" if current_player == "Maria" else "Maria"
