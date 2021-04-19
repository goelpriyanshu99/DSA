from math import sqrt
s = input()
res = set()

for i in range(len(s)-2):
    val1 = int(s[i:i+2])
    val2 = int(s[i:i+3])
    for val in [int(i), val1, val2]:
        j = int(sqrt(val))
        if j*(j+1) == val:
            res.add(val)

# for last second, last value and last 2 digits values
for j in [s[-2], s[-1], s[-2:]]:
    val = int(sqrt(int(j)))
    if val*(val+1) == int(j):
        res.add(int(j))

res -= {0}
res = list(res)
res.sort()
if(len(res)):
    print(*res, sep=',')
else:
    print(-1)