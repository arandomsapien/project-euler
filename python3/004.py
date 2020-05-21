# Solution to problem 4
# https://projecteuler.net/problem=4

def palindrome_check(n):
    """ Returns true if the number is the same forwards as backwards """

    # turn it into a string
    temp = str(n)

    length = len(temp)
    iter = 0

    # TODO this doesn't need to run for the entire string...
    while iter < len(temp):
        if temp[iter] != temp[length-1-iter]:
            return False

        iter += 1

    return True

a = 100
b = 100

largest_palindrome = 0

while a < 1000:
    while b < 1000:
        temp_product = a*b

        if palindrome_check(temp_product) == True:
            if temp_product > largest_palindrome:
                largest_palindrome = temp_product
                print("New winner! = {}".format(largest_palindrome))
        
        b += 1
    a += 1
    b = 100