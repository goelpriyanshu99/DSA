def check_paranthesis(inp):
    stack = []
    c = 1
    for i in inp:
        if i in ['(','[','{']:
            stack.append(i)
            c += 1
        else:
            if len(stack) == 0:
                return c
            elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
                stack.pop()
                c += 1
            else:
                return c
    return 0
        
if __name__ == "__main__":
    inp = input()
    print(check_paranthesis(inp))
    
''' got a string containing {,},[,],(,). you have to check that the paranthesis are balanced or not.
  if yes than print 0 else print the index+1 value where error occurs
  
input
1. {([])}[]
2. {{[]}}} 

output

1. 0
2. 7 '''