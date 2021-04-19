def rev(n):
    return int(str(n)[::-1])

def pall(n):
    return n == rev(n)

def small(n):
    if n <= 0:
        return 0
    return n if pall(n) else small(n-1)

def large(n):
    return n if pall(n) else large(n+1)

if __name__ == '__main__':
    innum = int(input())
    num1 = small(innum -1)
    num2 = large(innum + 1)
    outnum = num1 + num2
    # print(num1, num2)
    while not pall(outnum):
        innum -= 1
        if innum <= 0:
            outnum = 0
            break
        num1 = small(innum -1)
        num2 = large(innum + 1)
        # print(num1, num2)
        outnum = num1 + num2
    print(outnum)

    
'''Input innum. Calculate the largest pallindrome smaller than innum and smaller pallindrome larger than innum. Check 
    whether it's sum is pallindrome or not. Else repeat the process by decreasing innum by 1. Output the sum which is
    pallindrome

Input:
1. 152 
2. 4

Output:
1. 292
2. 8 '''

