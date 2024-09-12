from Bio.Seq import Seq
my_seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"


def count_seq(seq):
    A = my_seq.count('A')
    C = my_seq.count('C')
    G = my_seq.count('G')
    T = my_seq.count('T')
    return(A,C,G,T)

print(count_seq(my_seq))
