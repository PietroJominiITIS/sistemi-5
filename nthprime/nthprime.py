"""
Scrivere un programma Python che dato n trovi l'n-esimo numero primo.
"""

from math import sqrt, floor

memoization_table = {}
memoization_table['isPrime'] = {}
memoization_table['nthPrime'] = {}

memoization_count = {}
memoization_count['isPrime'] = [0, 0]
memoization_count['nthPrime'] = [0, 0]

def isPrime(n):
    """
    Check if a number is prime
    """
    # Memoization lookup
    if n in memoization_table['isPrime']:
        memoization_count['isPrime'][0] += 1
        return memoization_table['isPrime'][n]
    memoization_count['isPrime'][1] += 1

    # Actual algorithm
    for t in range(2, floor(sqrt(n)) + 1):
        if n % t == 0:  # The nuber has a divisor
            # Memoization saves
            memoization_table['isPrime'][n] = False 
            return False

    # Memoization saves
    memoization_table['isPrime'][n] = True          
    return True

def nthPrime(n):
    """
    Find the nth prime number
    """
    # Memoization lookup
    if n in memoization_table['nthPrime']:
        memoization_count['nthPrime'][0] += 1
        return memoization_table['nthPrime'][n]
    memoization_count['nthPrime'][1] += 1

    # Actual algorithm
    n_numbers = 0
    k = 2
    while n_numbers < n - 1:
        k += 1
        if isPrime(k):
            n_numbers += 1

    # Memoization saves
    memoization_table['nthPrime'][n] = k
    return k

def load_test_data():
    """
    Loads primes from primes.txt file
    """
    data = []
    with open('primes.txt') as primes:
        for line in primes.readlines():
            data += [int(n.strip()) for n in line.split()]
    return data

if __name__ == "__main__":

    # Number of test cases to test (max effective 10000)
    cases_number = 10001

    # Testing
    for n, expected in enumerate(load_test_data()[:cases_number]):
        assert expected == nthPrime(n + 1)
        print(f'Elaborating {floor(100*n/(cases_number - 1))}', end='\r')

    # Stats out
    isPrime_mem_perc = memoization_count["isPrime"][0] / (memoization_count["isPrime"][0] + memoization_count["isPrime"][1])
    nthPrime_mem_perc = memoization_count["nthPrime"][0] / (memoization_count["nthPrime"][0] + memoization_count["nthPrime"][1])
    print(f'Memomized {round(100 * isPrime_mem_perc, 2):3.2f}% \tof isPrime  calls')
    print(f'          {round(100 * nthPrime_mem_perc, 2):3.2f}% \tof nthPrime calls')