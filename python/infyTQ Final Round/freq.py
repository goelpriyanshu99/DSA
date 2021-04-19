arr = list(map(int, input().split(',')))
freq = [0]*10
for i in arr:
    freq[i] += 1

c = 0
l = []
for i in range(10):
    if freq[i] > 1:
        c += 1
        l.append(i)

print(c)
if c > 0:
    print(l)