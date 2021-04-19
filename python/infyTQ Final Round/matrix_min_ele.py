def matrix_calc():
    m,n = map(int, input().split())
    matrix = []
    for i in range(m):
        x = list(map(int,input().split()))
        matrix.append(x)
    res = set()
    for i in range(m):
        for j in range(n):
            
            # ROW CONSTRAINT
            if j < n-3 and matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3]:
                res.add(matrix[i][j])
            
            # COLUMN CONSTRAINT
            if i < m-3 and matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]:
                res.add(matrix[i][j])
            
            # DIAGONAL CONSTRAINT (BOTTOM TO TOP , LEFT TO RIGHT)
            if i >= 3 and j < n-3 and matrix[i][j] == matrix[i-1][j+1] == matrix[i-2][j+2] == matrix[i-3][j+3]:
                res.add(matrix[i][j])
            
            #DIAGONAL CONSTRAINT ()
            if j >= 3 and i >= 3 and matrix[i][j] == matrix[i-1][j-1] == matrix[i-2][j-2] == matrix[i-3][j-3]:
                res.add(matrix[i][i])
    
    res = list(res)
    return min(res) if len(res) != 0 else -1
    
if __name__ == "__main__":
    ans = matrix_calc()
    print(ans)
    
'''given no of rows m and cols n and an m*n size matrix find a no which is consecutively 
   repeating itself 4 times either in rowwise, columnwise or diagonal. Print the minimum if 
   many elements are present. If no element is present than print -1

Input:
1.  6 6 
    1 3 3 3 3 9 
    1 6 9 2 3 9
    1 2 2 5 4 9
    2 2 4 5 7 9
    2 4 5 6 7 2
    1 2 3 4 5 6

Output:
1. 2 '''
