from itertools import permutations
n=7
perm_list = list(permutations(range(1, n+1)))
print(perm_list)

n = 7
p = []

for number in range(1,n+1):
    p.append(number)

perm = permutations(p, n)

count = 0
perm_list = []


for i in perm:
    print(*i)
    count+=1

print(count)
