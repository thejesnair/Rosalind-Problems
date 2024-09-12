#code could be improved for speed

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


if __name__ == '__main__':
    
    with open('test data.txt') as file:
        for seq_id, seq in file_reader(file):
            seq_list.append(seq)
    
    srtd_seq = sorted(seq_list, key=len)
    key_seq = srtd_seq[0] #motif cannot be longer than shortest sequence
    comp_seq = srtd_seq[1:] #contains other sequences to compare against shortest sequence
    motif = ''
    
    for i in range(len(key_seq)):
        for j in range(len(key_seq)):
            key_motif = key_seq[i:j +1] #creates slice to compare, slices become larger as motif grows
            motif_found = False #most difficult part of code, being able to take slices and compare
            for seq in comp_seq:
                if key_motif in seq:
                    motif_found = True
                else:
                    motif_found = False
                    break
            if motif_found and len(key_motif) > len(motif):
                motif = key_motif
    print(motif)
