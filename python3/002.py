even_fib_sum = 2

# Getting started
a = 1
b = 2

# TODO make this better...

while (a + b) < 4000000:
    c = a+b

    if c % 2 == 0:
        even_fib_sum += c
    
    a = b
    b = c

print(even_fib_sum)