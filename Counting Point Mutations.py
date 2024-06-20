DNA1 = "GAGCCTACTAACGGGAT"
DNA2 = "CATCGTAATGACGGCCT"

def mutation(string1, string2):
    point_mutation = 0
    for x,y in zip(string1, string2):
        if x != y:
            point_mutation += 1
    return point_mutation

print(mutation(DNA1, DNA2))
