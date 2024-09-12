#overlap sequences, so length of k suffix matches length of k prefix

##from Bio import SeqIO
##seq_dict = {rec.id : rec.seq for rec in SeqIO.parse("rosalind_cons.txt", "fasta")}
##print(seq_dict)

import itertools

seq_list = []
seq_id_list = []

def file_reader(file):
    seq_id, seq = None, []
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            if seq_id: yield(seq_id, ''.join(seq))
            seq_id, seq = line[1:], []
            seq_id_list.append(seq_id)
        else:
            seq.append(line)
            
    if seq_id : yield (seq_id, ''.join(seq))


def does_k_overlap(s1, s2, k): #checks to see if k suffix/prefix match between s1, s2
    return s1[-k:] == s2[:k] #last three of s1 ==  first three of s2
    #returns T/F if matching

def k_edges(data, k):
    edges = [] #referring to suffix/prefix
    for u,v in itertools.combinations(data,2): #r length tuples, sorted order
        #u,v combinations of seq id in fasta file, to compare k below
        u_dna, v_dna = data[u], data[v] #pulls seq from data using seq id
        if does_k_overlap(u_dna, v_dna, k):
            edges.append((u,v))
        if does_k_overlap(v_dna, u_dna, k):
            edges.append((v,u))
        #reason we do u,v and v,u is because R_1234 R_1235 is different than R_1235 R_1234

    for pair in edges:
        print(str(pair).replace('(', '').replace(')','').replace(',','').replace("'", '').replace("'",''))

if __name__ == '__main__':
    
    with open('rosalind_grph.txt') as file:
        for seq_id, seq in file_reader(file):
            seq_list.append(seq)

        
    seq_dict = dict(zip(seq_id_list, seq_list))
    k_edges(seq_dict, k=3)
