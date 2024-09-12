from Bio.Seq import Seq

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

seq_list = []
count = 0

with open('test data.txt') as file:
    for seq_id, seq in file_reader(file):
        seq_list.append(seq)

for code in seq_list:
    dna = Seq(code)
    reverse_complement = dna.reverse_complement()
    if dna == reverse_complement:
        count +=1
    else:
        continue
print(count)
