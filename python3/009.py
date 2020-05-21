# Solution for problem 9
# https://projecteuler.net/problem=9

import math

def check_pytha_triplet(a,b):
    c = a**2 + b**2
    
    c = math.sqrt(c)

    if c.is_integer() == False:
        return False

    if a**2 + b**2 == c**2:
        return a,b,c

a = 1
b = 2

while a < 999:
    while b < 1000:
        if check_pytha_triplet(a,b):
            _a, _b, _c = check_pytha_triplet(a,b)

            if _a + _b + _c == 1000:
                print(int(_a * _b * _c))

        b += 1

    a += 1
    b = a+1