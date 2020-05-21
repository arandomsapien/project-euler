# Solution to problem 5
# https://projecteuler.net/problem=5

current_num = 20 # may as well start here
divisor = 20
best_divisor = 20

# I think I solved this a bit backwards, which seemed more fun than by divisors in ascending order

while divisor > 0:
    if current_num % divisor == 0:
        if divisor < best_divisor: 
            best_divisor = divisor
            print("Best so far! {} is divisible by all numbers down to {}".format(current_num, best_divisor))
        divisor -= 1
        continue
    else:
        current_num += 1
        divisor = 20
        continue

print("found it! {}".format(current_num))