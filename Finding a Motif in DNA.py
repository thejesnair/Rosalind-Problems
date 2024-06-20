DNA = "GATATATGCATATACTT"
motif = "ATAT"


for position in range(len(DNA)):
    #from position->onwards, does it start with motif?
    if DNA[position:].startswith(motif):
        #add 1 to position bc 0 based indexing
        print(position+1)
