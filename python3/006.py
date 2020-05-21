# Solution to problem 6
# https://projecteuler.net/problem=6

def sum_of_squares(n):
    """ returns the sum of squares of first n numbers """

    iter = 1
    
    sum = 0

    while iter <= n:
        sum += iter**2
        iter += 1
    
    return sum

def square_of_sums(n):
    """ returns the square of sums of first n numbers """

    iter = 1
    
    sum = 0

    while iter <= n:
        sum += iter
        iter += 1
    
    return sum**2

print(square_of_sums(100) - sum_of_squares(100))