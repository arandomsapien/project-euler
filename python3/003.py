import math

def prime_factors(n): 
    """ return a list prime factors for n """
    
    prime_factors = []

    while n % 2 == 0: 
        prime_factors.append(2)
        n = n / 2
    
    # int(math.sqrt(n))+1 is the max to test
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0: 
            prime_factors.append(i)
            n = n / i

    # Left over prime
    if n > 2: 
        prime_factors.append(n)
    
    return prime_factors

print(prime_factors(600851475143))