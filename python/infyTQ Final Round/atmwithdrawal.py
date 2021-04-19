n = int(input())
cash = []

for i in range(n):
    cash.append(int(input()))

to_withdraw = int(input())
s,e = 0,n-1
count = 0

if sum(cash) < to_withdraw:
    print(-1)
    exit(0)

while to_withdraw > 0:
    if cash[s] == to_withdraw or cash[e] == to_withdraw:
        to_withdraw = 0
        count += 1
        continue

    m = max(cash[s],cash[e])
    if m < to_withdraw:
        if m == cash[s]:
            s += 1
        else:
            e -= 1
    
        to_withdraw -= m
        count += 1
    else:
        count = -1
        break

print(count)
    
''' You have been given n size of atm and n-line separted money in atm and x amount to withdraw. You only can 
    withdraw money from any one end of array. Print how much withdraw are needed to withdraw amt x, if not possible print -1

Input:
1.  4
    2
    3
    5
    5
    10
2.  2
    1
    1
    3

Output:
1.  2
2.  -1 '''