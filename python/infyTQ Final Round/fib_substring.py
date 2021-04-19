def calc_fib():
    l = set(map(int,input().split(',')))
    max_ele = max(l)
    fib = {0,1}
    a,b = 0,1
    while max(fib) <= max_ele:
        fib.add(a+b)
        a,b = b,a+b
    ans = l.intersection(fib)
    return len(ans) if len(ans) > 2 else -1 
    
if __name__ == "__main__":
    ans = calc_fib()
    print(ans)
    
''' Given a string with no separated by comma(,) You have to calculate the substring which have 
    fibonacci no. If such elements are more than 2 print it's length else -1

Input:
1. 3,2,5,8,9,10,11
2. 2,6,3,5,8,9

Output:
1. 4
2. 4 '''
