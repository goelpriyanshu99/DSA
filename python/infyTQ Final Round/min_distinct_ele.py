from collections import defaultdict as dd
from itertools import accumulate as ac

def main():
    ele = int(input())
    l = list(map(int,input().split()))
    d = dd(int)
    for i in l:
        d[i] += 1
    freq = [x for x in d.values()]
    freq.sort()
    res = list(ac(freq))
    for i in range(len(res)):
        if res[i] == ele:
            return len(res) - i - 1
        elif res[i] > ele:
            return len(res) - i
    return 0
    

if __name__ == "__main__":
    distinct = main()
    print(distinct)
    
'''given a number n and list l. n denotes no of elements to be deleted from list l such that 
   there are minimum distinct elements in the list.

Input:
1.  4
    1 1 1 2 2 3 3 4 5 6
2.  3
    1 1 1 2 2 2 4 5 6

Output:
1. 3
2. 2 '''
