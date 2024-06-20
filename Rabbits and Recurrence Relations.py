https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jPMKByWX0p7Q0zGzh_lzdw.png
#illustrates population growth
#M1: 1 pair
#M2: Able to reproduce
#M3: 1 old pair, 2 new 
https://miro.medium.com/v2/resize:fit:1400/format:webp/1*p4hQbk3Y3qvID17p-9Xtvg.png
#illustrates pop growth after 5 months

def rabbits_present(months, litter):
    F1 = 1
    F2 = 1 #constants
    for n in range(months - 2): #rabbits reach reproductive age after one month 
        F3 = F1*litter+F2 #1*3+1=4 rabbit pairs, starting one pair
        #The number of offspring in any month is EQUAL to the number of rabbits that were alive two months prior.
        F1 = F2 
        F2 = F3
    return F3

print(rabbits_present(5,3))
print(rabbits_present(32,3))
