def rev(n):
    return int(str(n)[::-1])

def check_pallindrome(n):
    return n == rev(n)

def res(n):
    reverse = rev(n)
    n += reverse
    return n if check_pallindrome(n) else res(n)


if __name__ == '__main__':
    n = int(input())
    print(res(n))

'''Calculate the pallindrome no from given no by adding reverse to it.

Input:
1. 195 
2. 4

Output:
1. 9339
2. 8 '''

