rosalind_6404 = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
rosalind_5959 = "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
rosalind_0808 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

def GC_content(sequence):
    G=0
    C=0
    total_bases = 0
    for nucleobase in sequence:
        total_bases += 1
        if nucleobase == "G":
            G += 1
        elif nucleobase == "C":
            C += 1
        else:
            continue
    return ((G+C)/total_bases*100)

GC_dict = {'rosalind_6404': GC_content(rosalind_6404), \
           'rosalind_5959': GC_content(rosalind_5959), \
           'rosalind_0808': GC_content(rosalind_0808)}

print(GC_dict)
print(max(GC_dict.items(), key=lambda x:x[1]))

#code that takes into consideration actual dataset file
file = open('rosalind_gc_2_dataset.txt', 'r')

max_gc_id = '' #string for ID name containing max GC content
max_gc_content = 0 #percentage max GC content
dataset = file.readline().rstrip() #read file one line, strip end

while dataset:
    seq_name = dataset[1:] #pull everything after index 1, after >
    seq = '' #empty string name to hold DNA further down in code
    dataset = file.readline().rstrip() #loads next line after seq ID
    #code to loop through lines of each sequence and add to a string
    while not dataset.startswith('>') and dataset: #so while line doesnt start > and part of dataset
        seq = seq + dataset #add DNA string to variable
        dataset = file.readline().rstrip() #assign next line to variable, "looping" through
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq)) #amount GC content for seq above
    if seq_gc_content > max_gc_content:
        max_gc_id = seq_name #assign name of ID to max id
        max_gc_content = seq_gc_content #assign content of max sequence to max variable

print('%s\n%.6f%%' % (max_gc_id, max_gc_content * 100))
file.close()

#format string
#%s add value into python string
#%.6f%% percentage and 6 values after decimal place
#% modulo operator
#corresponding values
