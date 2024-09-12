from collections import defaultdict

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

with open('rosalind_cons.txt') as file:
    for seq_id, seq in file_reader(file):
        seq_list.append(seq)


#create matrix for each string
n = 0 #count of bases in each string
for string in seq_list[0]:
    for base in string:
        n += 1

matrix = {
    'A' : [0]*n,
    'C' : [0]*n,
    'G' : [0]*n,
    'T' : [0]*n
    }

#count nt in each position for each base
for string in seq_list:
    for position, base in enumerate(string): #enumerate creates tuple, index and value
        matrix[base][position] += 1 #counts

#reformat matrix into n x 4
matrix_1 = ('\n'.join("{}: {}".format(k, v) for k, v in matrix.items()))
#reformat matrix without , or []
matrix_2 = str(matrix_1).replace('[', '').replace(']', '').replace(',', '')



#create consensus string
consensus_list = []

for position in range(n):
    max_count = 0
    max_base = None
    for base in ['A', 'C', 'G', 'T']:
        count = matrix[base][position]
        if count > max_count:
            max_count = count
            max_base = base
    consensus_list.append(max_base)


consensus_string = ''.join(consensus_list)

print(consensus_string)
print(matrix_2)
