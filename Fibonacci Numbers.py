##1, 1, 2, 3, 5, 8...
def fib(number):
    #first two digits in fibonacci sequence
    initial_digit, next_digit = 1,1
    for int in range(number-1):
        next_digit, initial_digit = initial_digit, initial_digit + next_digit
    return next_digit
        
print(fib(22))
