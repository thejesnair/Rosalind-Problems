"""
Need to quantify the likelihood of finding a given motif randomly.
Form model for creating genomes randomly, calculate the probability that a motif occurs randomly at a fixed location in the genome.

Array contains ordered colection of objects, like a matrix but only one row.
Random strings are constructed so the prob. of choosing each subsequent string is based on a fixed underlying symbol freq.
GC-content offers natural symbol freq. for making random DNA strings. If GC-content is x, then set symbol freq of C and G to x/2 and
A and T to (1-x)/2
    if GC-content is 40%, next symbol is G/C with prob of 0.2 and next symbol is A/T with prob of 0.3

Use log function to make comparison easier.

code partially adapted from unknown source
"""
from math import log10

with open('rosalind_prob.txt') as input_data:
    dna, gc_content = input_data.readlines() #given DNA string, array 

gc_content = map(float, gc_content.split()) #map() applies fxn to every item of iterable

codon_count = [0,0]
for codon in dna:
    if codon in ['G', 'C']:
        codon_count[0] += 1
    elif codon in ['A', 'T']:
        codon_count[1] += 1

gc_prob = []
for value in gc_content:
    log_prob = codon_count[0]*log10(0.5*value) + codon_count[1]*log10(0.5*(1-value))
    gc_prob.append(str(log_prob))

gc_prob = ' '.join(gc_prob)

print(gc_prob)
