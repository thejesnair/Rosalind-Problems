"""
Punnett Square Breakdown
AA x AA = 100% AA
AA x Aa = 50% AA 50% Aa
AA x aa = 100% Aa
Aa x AA = 100% AA
Aa x Aa = 25% AA, 50% Aa, 25% aa
Aa x aa = 50% Aa, 50% aa
aa x AA = 50% Aa, 50% aa

Ex: k=2,m=2,n=2
total=6
k = dominant
m = hetero
n = recessive

Probablility Breakdown (without replacement)
kk = 2/6 * 1/5      100% dominant
km = 2/6 * 3/5      100% 
kn = 2/6 * 3/5      100%
mk = 2/6 * 3/5      100%
mm = 2/6 * 1/5      75% (refer to PS)
mn = 2/6 * 3/5      50%
nk = 2/6 * 3/5      100%
nm = 2/6 * 3/5      50%
nn = 2/6 * 1/5      0%
"""

dominant = 15
hetero = 18
recessive = 15
def dominant_probability(dominant, hetero, recessive):
    total = dominant + hetero + recessive
    #determine percentages RECESSIVE PHENOTYPE for possible genotypes
    recessive_prob = (recessive/total) * ((recessive - 1)/(total - 1))
    #multiplied by 0.25 bc 25% recessive probability with 2 hetero GT
    hetero_prob = (hetero/total) * ((hetero - 1)/(total-1))* 0.25
    #multiplied by 0.5 bc 50% recessive prob with hetero x rec GT
    hetero_recessive = ((hetero/total) * (recessive/(total-1)) + \
                       (recessive/total) * (hetero/(total-1))) * 0.5

    recessive_total = recessive_prob + hetero_prob + hetero_recessive

    return(1-recessive_total)

print(dominant_probability(dominant, hetero, recessive))
