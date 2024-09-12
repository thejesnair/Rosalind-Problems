from math import factorial
#A-U, G-C pairs
#perfect matchings number of matchings in first graph (bipartite graphs) * second

sequence = 'AGCUAGUCAU'

result = factorial(sequence.count('A')) * factorial(sequence.count('C'))

print(result)
