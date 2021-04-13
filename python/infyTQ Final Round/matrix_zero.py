def calc_arr(arr,t):
    row, col = [] , []
    for i in range(t):
        if 0 in arr[i]:
            row.append(i)
            for j in range(t):
                if arr[i][j] == 0:
                    col.append(j)
        
    for i in row:
        for j in range(t):
            arr[i][j] = 0

    for i in set(col):
        for j in range(t):
            arr[j][i] = 0

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        x = list(map(int,input().split()))
        arr.append(x)

    calc_arr(arr,n)

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()



'''Input             Output
  4                  0 0 0 0
  2 3 0 6            0 0 0 0
  1 2 3 0            9 6 0 0 
  9 6 2 5            1 2 0 0 
  1 2 3 4  '''              
                
                
                


