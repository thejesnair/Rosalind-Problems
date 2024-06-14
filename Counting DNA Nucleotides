#test
#test_DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

#dataset
file = open('rosalind_dna_1_dataset.txt', 'r')
DNA = file.read()
file.close()

A = 0
C = 0
G = 0
T = 0

for nucleobase in DNA:
    if nucleobase == "A":
        A += 1
    elif nucleobase == "C":
        C += 1
    elif nucleobase == "G":
        G += 1
    elif nucleobase == "T":
        T += 1

A = DNA.count("A")
C = DNA.count("C")
G = DNA.count("G")
T = DNA.count("T")

print(A,C,G,T)
