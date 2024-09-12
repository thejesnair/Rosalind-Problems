seq_list = []

def file_reader(file):
    seq_id, seq = None, []
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            if seq_id: yield(seq_id, ''.join(seq))
            seq_id, seq = line, []
        else:
            seq.append(line)
    if seq_id : yield (seq_id, ''.join(seq))

with open('test data.txt') as file:
    for seq_id, seq in file_reader(file):
        seq_list.append(seq)



seq_1= seq_list[0]
seq_2= seq_list[1]

#transition when no change in base structure (A--G, T--C)
#transverion when one purine for pyrimidine, change in structure

purine = ['A', 'G']
pyrimidine = ['C', 'T']

transition = 0
transversion = 0
for nb1, nb2 in zip(seq_1, seq_2):
    if nb1 != nb2:
        if (nb1 in purine and nb2 in purine) or (nb1 in pyrimidine and nb2 in pyrimidine):
            transition +=1
        else:
            transversion +=1

print(transition/transversion)
