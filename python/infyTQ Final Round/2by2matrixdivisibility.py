def calc_no(val):
    temp = val
    s = 0
    while temp > 0:
        s += temp%10
        temp //= 10
    return not(val%s)

row = int(input())
arr = []  # storing input values
for i in range(row):
    arr.append(list(map(int,input().split())))
bool_tab = []  # storing their resp boolean value if it is divisible by the sum of digits than True else False
for i in range(row):
    x = []
    for j in range(len(arr[0])):
        x.append(calc_no(arr[i][j]))
    bool_tab.append(x)
res = []
for i in range(row-1):
    for j in range(len(arr[0])-1):
        if bool_tab[i][j] and bool_tab[i][j+1] and bool_tab[i+1][j] and bool_tab[i+1][j+1]:
            res.append([arr[i][j], arr[i][j+1],arr[i+1][j],arr[i+1][j+1]])
if len(res) > 0:
    for i in res:
        print(i[0], i[1])
        print(i[2], i[3])
        print()
else:
    print('No matrix found')

''' Input
    3
    42 54 2
    30 24 27
    180 190 40

    Output
    42 54
    30 24

    54 2
    24 27

    30 24
    180 190

    24 27
    190 40'''