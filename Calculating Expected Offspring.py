"""
1. AA-AA, 100% dom pt
2. AA-Aa, 100%
3. AA-aa, 100%
4. Aa-Aa, 75%
5. Aa-aa, 50%
6. aa-aa, 0%

"""

data = [19254, 18452, 17286, 17274, 16766, 18621]

dominant_pt = [2.0, 2.0, 2.0, 1.5, 1.0, 0.0] #dom phenotypes * 2 offspring

with open('rosalind_iev.txt', 'r') as file:
    dataset = [int(x) for x in file.read().split()]
    print(dataset)

print(sum([x*y for x,y in zip(dominant_pt, dataset)]))
#zip both lists paired together
