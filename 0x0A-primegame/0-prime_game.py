#!/usr/bin/python3
"""It's gaming time!"""


def get_prime(n):
    """Return a list of prime numbers within a certain range"""
    if n == 1:
        return ([])
    my_primes = []
    list_primes = [i for i in [2, 3, 5, 7] if i <= n]
    for i in range(2, n + 1):
        is_ = 0
        for n in list_primes:
            if i % n == 0 and n < i:
                is_ = 1
                break
        if is_ == 0:
            my_primes.append(i)
    return (my_primes)


def isWinner(x, nums):
    """Determine winner of game"""
    ben = 0
    maria = 0
    for rnd in nums:
        prime_list = get_prime(rnd)
        person = 1
        list_nums = [i for i in range(1, rnd + 1)]
        while True:
            if len(prime_list) == 0:
                if person % 2 == 1:
                    ben += 1
                else:
                    maria += 1
                break
            choice = min(prime_list)
            prime_list.remove(choice)
            bef_len = len(list_nums)
            for num in list_nums:
                if num % choice == 0:
                    list_nums.remove(num)
    if maria == ben:
        return None
    if maria > ben:
        return ('Maria')
    else:
        return ('Ben')
