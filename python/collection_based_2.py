# https://www.interviewbit.com/problems/collections-module-ii/
from collections import OrderedDict as od
from collections import Counter as c
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    l = []
    price = od()
    for i in range(N):
        k,v = map(int,input().split())
        price[k] = v
        l.append(k)
    qty = c(l)
    for i in price.keys():
        print(i, price[i]*qty[i], end= " ")
        print()
    return 0

if __name__ == '__main__':
    main()
