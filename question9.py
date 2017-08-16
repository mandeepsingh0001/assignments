# QUESTION 9 (count the upper and lower cases)

s = raw_input("enter string :")

U = L = 0

for c in s:
    if c.isupper():
        U=U+1
    elif c.islower():
        L=L+1
    else:
        pass

print("upper = ",U)
print("lower = ",L)