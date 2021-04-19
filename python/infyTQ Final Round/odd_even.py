def calc_outstr():
    inp = input()
    c = 0
    odd, even = [], []
    for i in inp:
        if not i.isalnum():
            c += 1
        elif i.isdigit():
            if int(i)%2 == 0:
                even.append(i)
            else:
                odd.append(i)
                
    if c%2 != 0:
        even, odd = odd, even
        
    s = ''
    i = 0
    while i<len(even) and i<len(odd):
        s += even[i] + odd[i]
        i += 1 
    s += ''.join(even[i:]) + ''.join(odd[i:])
    return s
    
if __name__ == "__main__":
    ans = calc_outstr()
    print(ans)
    
''' Given a string with atleast 1 special char, 1 odd no and 1 even no. If even no of special
    char are present than return a string with even and odd no alternatively starting with even
    no. similarly for odd no.

Input:
1. a5c67r21i@p#8t
2. h93@5213#w4rld&

Output:
1. 652781
2. 9234513 '''
