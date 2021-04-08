from itertools import permutations as p
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    s,k = input().split()
    l = list()
    for i in p(s,int(k)):
        l.append(''.join(i))
    l.sort()
    for i in l:
        print(i)
    return 0

if __name__ == '__main__':
    main()