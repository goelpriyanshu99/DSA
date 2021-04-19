def find(key,val, x):
    l = [int(i) for i in val]
    l.sort(reverse=True)
    for i in l:
       if i <= x:
           return key[i-1]
    else:
        return 'X'

def special(d):
    password = ''
    for i in d.keys():
        x = len(i)
        password += find(i,d[i],x)
    return password
    
if __name__ == "__main__":
    inp = input().split(',')
    d = dict()
    for i in inp:
        name,code = i.split(':')
        d[name] = code
    print(special(d))
    
''' got a string as input with name and code. Print the string having 1 character from all 
    the names using condition as use the value of code having value <= len of resp. name 
    else use X as the char.
  
input
1. Anchal:23581,Aman:57568,Sonakshi:34848,Ria:14585
2. Sonakshi:34848,Naman:4739,Prachi:2949,Ekta:9889

output

1. aXiR
2. iacX'''