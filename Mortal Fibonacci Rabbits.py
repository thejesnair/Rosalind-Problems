#https://duphan.wordpress.com/2015/07/10/dynamic-programming-and-mortal-fibonacci-rabbits/

def fib_mortal(n,k=1): #k is breeding pairs
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)
