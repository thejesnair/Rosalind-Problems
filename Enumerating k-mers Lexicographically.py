import itertools

alpha = 'ABCDE'
n = 4
combo = [i for i in itertools.product(alpha,repeat=n)]

for item in combo:
    for i in range(0, int(n/2)):
        print(str(item[i]) + str(item[i+1]))
