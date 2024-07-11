https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jPMKByWX0p7Q0zGzh_lzdw.png
#illustrates population growth
#M1: 1 pair
#M2: Able to reproduce
#M3: 1 old pair, 2 new 
https://miro.medium.com/v2/resize:fit:1400/format:webp/1*p4hQbk3Y3qvID17p-9Xtvg.png
#illustrates pop growth after 5 months

#solution utilizes traditional fib sequence/pattern, easier to understand
def fib_rabbits(months, offspring):
    parent, child = 1,1
    for int in range(months-1):
        child, parent = parent, parent + (child*offspring) 
        #multiply by offspring, beginning with 1 pair, producing litter of k
        #rabbit pairs instead of 1 pair
    return(child)

print(fib_rabbits(5,3))
print(rabbits_present(32,3))
