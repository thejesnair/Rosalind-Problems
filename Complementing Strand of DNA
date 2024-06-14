#test
#test_DNA = "AAAACCCGGT"

#dataset
file = open('rosalind_revc_1_dataset.txt', 'r')
DNA = file.read()
file.close()

def reverse(DNA):
    DNA = DNA[::-1]
    return DNA

def complement(DNA):
    DNA = reverse(DNA)
    reverse_complement = ""
    for nucleobase in DNA:
        if nucleobase == "A":
            reverse_complement += "T"
        elif nucleobase == "T":
            reverse_complement += "A"
        elif nucleobase == "G":
            reverse_complement += "C"
        elif nucleobase == "C":
            reverse_complement += "G"
    return reverse_complement

print(complement(DNA))
