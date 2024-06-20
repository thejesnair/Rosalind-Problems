#test code with sampel set
DNA1 = "GAGCCTACTAACGGGAT"
DNA2 = "CATCGTAATGACGGCCT"

def mutation(string1, string2):
    point_mutation = 0
    for x,y in zip(string1, string2):
        if x != y:
            point_mutation += 1
    return point_mutation

print(mutation(DNA1, DNA2))

#alternative code for dataset
with open('rosalind_hamm_1_dataset.txt', 'r') as file:
    point_mutation = 0
    DNA1 = file.readline().strip() #strip leading and tailing white space
    DNA2 = file.readline().strip()
    for x,y in zip(DNA1, DNA2):
        if x != y:
            point_mutation += 1
print(point_mutation)
