s = input()
l = []
[l.append(x) for x in s if x not in l]
print(''.join(l[::-1]))

# input string remove duplicates and print the reverse of string

# Input
# infosys
# Output
# ysofni
