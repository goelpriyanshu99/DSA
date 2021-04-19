m = int(input())
p = int(input())

inmatrix1, inmatrix2 = [], []
outmatrix = []

for i in range(m):
    inmatrix1.append(list(map(int,input().split())))
for i in range(p):
    inmatrix2.append(list(map(int,input().split())))

n = len(inmatrix1[0])
q = len(inmatrix2[0])

for i in range(m):
    x = []
    for j in range(n):
        x.append(0)
    outmatrix.append(x)

for i in range(m):
    for j in range(n):
        if i == j:
            if i <= p-1 and j <= q-1:      
                outmatrix[i][j] = inmatrix1[i][j]*inmatrix2[i][j]
            else:
                outmatrix[i][j] = -1
        else:
            temp = []
            if i < p and i < q:
                temp.append(inmatrix1[i][j]*inmatrix2[i][i])    #r1,r1
            if i < p and j < q:
                temp.append(inmatrix1[i][j]*inmatrix2[i][j])    #r1,c1
            if j < p and j < q:
                temp.append(inmatrix1[i][j]*inmatrix2[j][j])    #c1,c1
            if i < q and j < p:
                temp.append(inmatrix1[i][j]*inmatrix2[j][i])    #c1,r1
            
            if len(temp) == 0:
                outmatrix[i][j] = -1
            else:
                temp_set = set(temp)
                if len(temp_set) == len(temp):
                    val = min(temp)
                else:
                    c = temp.count(temp_set[0])
                    val = temp_set[0]
                    for ele in temp_set[1:]:
                        if c < temp.count(ele):
                            c = temp.count(ele)
                            val = ele
                            continue
                        if c == temp.count(ele) and c == 2:
                            val = min(temp)
                            break
                outmatrix[i][j] = val

for i in outmatrix:
    print(*i, sep=' ')


# +5-7
                    
                        
                
                
            
            