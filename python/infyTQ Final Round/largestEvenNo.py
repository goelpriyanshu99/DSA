s = input()
num = set()
even_s = 51 # any number greater than 9
temp = 51 # same as even_s
for i in s:
    if i.isdigit():
        if int(i)%2 == 0 and int(i)<even_s:
            num.add(str(even_s))
            even_s = int(i)
            continue
        num.add(i)
num -= {str(temp)} # remove 51 which was added str of even_s at line 7
num = list(map(int,num))
num.sort(reverse=True)
print(-1 if even_s == temp else ''.join(map(str,num))+str(even_s))

''' largest even no without duplicate digits from a string consisting 
  of letters, alphabets and numbers, if no such even no is present print -1 

Input
1.  asdf@75483
2. infytq351739

Output
1. 87534 
2. -1  '''




