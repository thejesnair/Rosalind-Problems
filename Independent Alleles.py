"""probability of at least N AaBb organism will belong to k-th generation of family tree, mendels second law holds:
alleles for diff factors are inherited with no dependence on each other"""

def independent_alleles():
    import math
    k = 2
    N = 1
    P = 2**k
    probability = 0
    for i in range(N, P+1):
        prob = (math.factorial(P)/
                (math.factorial(i)*math.factorial(P-i)))* (0.25**i)*(0.75**(P-i))
        probability += round(prob,3)
        
    return probability

print(independent_alleles())
