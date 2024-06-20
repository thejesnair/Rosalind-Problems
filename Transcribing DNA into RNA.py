#test
#test_genome = "GATGGAACTTGACTACGTAAATT"

#dataset
file = open('rosalind_rna_1_dataset.txt', 'r')
genome = file.read()
file.close()

RNA = ""

for nucleobase in genome:
    if nucleobase == "T":
        RNA = genome.replace("T", "U")

print(RNA)
