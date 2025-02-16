""" 25. Inferring mRNA from Protein """

""" Given protein string, return total number of RNA strings from which the protein could be translated, modulo 1,000,000
don't forget to include stop codon in translation """

"""
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G

example:
M (*1) + A (*4) + Stop (*3) = 12
output: 12
"""

with open('rosalind_mrna.txt', 'r') as aa_sequence:
    aa_sequence = aa_sequence.read().strip()


#dict of possible codons to amino acids

protein_rna_dict = {'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4}
stop_codons = ['UAA','UGA','UGA']
total_stop = 3

possible_rna = 1 #set to 1 to capture possible_rna strings down below

for aa in aa_sequence:
    possible_rna = (possible_rna * protein_rna_dict[aa]) % 1000000

possible_rna = (possible_rna * total_stop)

print(possible_rna)
