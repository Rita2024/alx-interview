#!/usr/bin/python3
"""The prime game module."""


def is_winner(rounds, numbers):
    """Determines the winner of a prime game session with `rounds` rounds and `numbers` for each round.

    Args:
        rounds: The number of rounds played.
        numbers: A list containing the maximum number for each round.

    Returns:
        The name of the winner ("Maria" or "Ben") or None if it's a tie.
    """

    if rounds < 1 or not numbers:
        return None

    maria_wins, ben_wins = 0, 0

    # Find the maximum number across all rounds for efficient prime sieve
    max_number = max(numbers)

    # Pre-compute primes using the Sieve of Eratosthenes
    primes = [True] * (max_number + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_number**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_number + 1, i):
                primes[j] = False

    # Count prime wins for each round efficiently
    for round_num, max_num in zip(range(rounds), numbers):
        prime_count = sum(primes[:max_num + 1])
        ben_wins += prime_count % 2 == 0
        maria_wins += prime_count % 2 == 1

    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"

