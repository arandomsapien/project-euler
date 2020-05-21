# Solution to problem 10
# https://projecteuler.net/problem=10

import math

def prime_test(n):
    """ returns True if n is prime """

    # 1 isn't prime 
    # https://www.youtube.com/watch?v=IQofiPqhJ_s
    if n <= 1: return False

    if n == 2: return True

    # Since I'm starting the test with 3...
    # I'm sure there's a better way to do this.
    # TODO Make a real primality test someday?
    if n == 3: return True
    
    # Not even? Not a prime.
    if n % 2 == 0: return False

    # Why test up to the square root? 
    # https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-prime-number-to-determine-if-it-is-pr
    test_limit = math.floor(math.sqrt(n))
    
    current_test = 3

    while current_test <= test_limit:
        if n % current_test == 0:        
            return False
        else:
            current_test += 2
            continue

    return True

primes = [2,3]

current = 5

while current <= 2_000_000:
    if prime_test(current) == True:
        primes.append(current)
    
    current += 2

print ("Done making all those primes... whew")

sum = 0
for num in primes:
    sum += num

print("sum of all those primes...")
print(sum)