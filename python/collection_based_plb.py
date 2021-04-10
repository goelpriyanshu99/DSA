# https://www.interviewbit.com/problems/collections-module-i/

from collections import defaultdict as dd
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    d = dd(int)
    x = list(map(int,input().split()))
    for i in x:
        d[i] += 1
    X = int(input())
    earning = 0
    for i in range(X):
        x,c = map(int, input().split())
        if(d[c] > 0):
            earning += x
            d[c] -= 1
    print(earning)
    return 0

if __name__ == '__main__':
    main()
