s = input()
vowel = ['a','e','i','o','u','A','E','I','O','U']
t = True
if s[0] in vowel:
    for i in range(0,len(s)-1,2):
        if not(s[i] in vowel and s[i+1] not in vowel):
            t = False
            break
    else:
        if len(s)%2 == 1 and s[i+2] not in vowel:
            t = False
else:
    for i in range(0,len(s)-1,2):
        if not(s[i] not in vowel and s[i+1] in vowel):
            t = False
            break
    else:
        if len(s)%2 == 1 and s[i+2] in vowel:
            t = False 

print('Valid' if(t) else 'Invalid')

''' Vowel and consonant alternetively   
iRiS
Valid

adedf
Invalid ''''