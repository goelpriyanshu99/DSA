n = int(input())
A, B = [], []
for i in range(n):
    A.append(int(input()))
for i in range(n):
    B.append(int(input()))

unpacked = 0
for cur in A:
    for j in range(n):
        if B[j] >= cur:
            B[j] = 0
            break
    else:
        unpacked += 1

print(unpacked)


''' given n and 2 arrays gifts(A) and boxs(B) of len n. Santa will pick a gift from A and search for a box in B which 
    is greater or equal to it. Now, print op how many gift left unpack. Santa will pick element from left to right


Input:
1.  3
    1
    23
    4
    2
    3
    4
2.  3
    1
    23
    4
    2
    5
    25

Output:
1. 1
2. 0  '''