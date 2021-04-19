s = input()
otp = ''
for i in range(1,len(s),2):
    otp += str(int(s[i])**2)
    if len(otp) >= 4:
        break
print(otp[:4])

# otp generation from odd places digit and appending their squares through string 

# Input
# 5624381275
# Output
# 3616

