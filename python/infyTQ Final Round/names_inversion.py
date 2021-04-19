def calc_new(d):
    new_s = []
    for k,v in d.items():
        [new_s.append(k[len(k)-2:] + k[:len(k)-2]) if v%2 == 0 else new_s.append(k[1:] + k[:1])]
    print(" ".join(new_s))
    
if __name__ == "__main__":
    inp = input().split(',')
    d = dict()
    for i in inp:
        name,code = i.split(':')
        temp = [int(i)**2 for i in code]
        d[name] = sum(temp)
    calc_new(d)
    
''' got a string as input with name and code. Print the string acc to given rules:
    calc sum of squares of each val of a particular code. 
    if sum is even then add last 2 chars of name at starting of name
    else add starting 1st char to last of name
  
input
1. abcd:1234,bcdgfhf:127836,sdjks:1245

output

1. cdab cdgfhfb kssdj
'''