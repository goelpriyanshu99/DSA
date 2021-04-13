inp = list(map(int,input().split(',')))
ind_4, ind_7 = inp.index(4), inp.index(7)
num1 = sum(inp[:ind_4]) + sum(inp[ind_7+1:])
num2 = ''.join(map(str,inp[ind_4:ind_7+1]))
print(num1+int(num2))

# num1 store addition of values before 4 and after 7
# num2 store the int of string from 4 to 7

# Input
# 2,5,6,4,2,3,7,8
# Output
# 4258
