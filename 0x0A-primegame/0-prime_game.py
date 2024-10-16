#!/usr/bin/python3


def isWinner(x, nums):
    """Determines the winner of the Prime Game."""
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to limit the sieve
    max_n = max(nums)

    # Step 1: Compute all primes up to max_n using the Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_n)

    # Step 2: Simulate each round of the game and determine winners
    maria_wins = 0
    ben_wins = 0

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
    """Generates a list of boolean values where True the index is prime."""
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False

    return is_prime


def simulate_game(n, primes):
    """Simulates a single round of the Prime Game."""
    # Create a list to track the available numbers (True if not removed)
    remaining_numbers = [True] * (n + 1)

    current_player = "Maria"  # Maria always starts

    while True:
        move_made = False
        # Find the next available prime in the range
        for i in range(2, n + 1):
            if remaining_numbers[i] and primes[i]:
                # Remove the prime and all its multiples
                for multiple in range(i, n + 1, i):
                    remaining_numbers[multiple] = False
                move_made = True
                break

        if not move_made:
            # No valid move can be made, current player loses
            if current_player == "Maria":
                return "Ben"
            else:
                return "Maria"

        # Switch players after a move
        if current_player == "Maria":
            current_player = "Ben"
        else:
            current_player = "Maria"
