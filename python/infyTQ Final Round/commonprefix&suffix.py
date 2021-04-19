def main():
    s = input()
    mid = len(s)//2

    for i in range(mid,-1,-1):
        prefix = s[:i]
        suffix = s[len(s)-i:]
        
        if prefix == suffix:
            print(i, prefix)
            break

if __name__ == "__main__":
    main()
    
    
'''given a string find the length of largest common prefix and suffix such that there is 
no common element present

Input:
1. abcdeabcd
2. abcba

Output:
1. 4 abcd
2. 1 a '''
