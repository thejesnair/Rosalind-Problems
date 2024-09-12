from Bio.Seq import Seq #biopython library

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

sequence = seq_list[0]
introns = seq_list[1:]
exons = []

for i in range(len(introns)):
    sequence = sequence.replace(introns[i], '')

sequence = Seq(sequence)

print(sequence.translate(to_stop=True))
