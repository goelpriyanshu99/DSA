from itertools import permutations as per
s = input()
for i in range(1,len(s)+1):
    for j in per(s,i):
        print(''.join(j))

''' asd
    a
    s
    d
    as
    ad
    sa
    sd
    da
    ds
    asd
    ads
    sad
    sda
    das
    dsa '''