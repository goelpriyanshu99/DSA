def calc_outstr():
    inpt = input()
    inp = [x for x in inpt]
    s,e = 0,len(inp)-1
    l = (e+1)//2 
    for i in range(l+1):
        if not inp[s].isalnum():
            s += 1 
            continue
        if not inp[e].isalnum():
            e -= 1 
            continue
        if s >= e:
            break
        inp[s],inp[e] = inp[e], inp[s]
        s += 1 
        e -= 1
    return ''.join(inp)
    
if __name__ == "__main__":
    ans = calc_outstr()
    print(ans)
    
''' Given a string with 1 special char. We have to reverse the string except changing the 
    position of special char

Input:
1. ra@am
2. pyth@on

Output:
1. ma@ar
2. noht@yp '''
