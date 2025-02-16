"""
Similar species will share many genes, but not all. Modify the notion of permutation to quatify partial gene orderings
Given n, k where 100 > n > 0 and 10 > k > 0, return total number of permutations modulo 1E6
"""

n = 21
k = 7

import itertools
import math

partial_permutation = math.perm(98, 9)
print(int(partial_permutation % 1E6))
