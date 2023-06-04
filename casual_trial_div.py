from math import sqrt
from millercheck import my_miller_rabin

def trial_division(n):
    if my_miller_rabin(n): 
        return [n]
    n = abs(n)
    result = [-1] if n < 0 else []
    if n < 0:
        result.append(-1)
        n *= -1
    primes = []
    m = int(sqrt(n))
    for i in range(2, m+1):
        if my_miller_rabin(i): 
            primes.append(i)
    i = 0
    while n > 1 and i < len(primes):
        if n % primes[i] == 0:
            while n % primes[i] == 0:
                result.append(primes[i])
                n //= primes[i]
        else:
            i += 1
    if n > 1 and my_miller_rabin(n): 
        result.append(n)
    return result
