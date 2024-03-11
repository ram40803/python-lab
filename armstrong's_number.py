n = int(input("enter a number:"))
n2 = 0

i = n
dig = 0
while i>0:
    dig += 1
    i //= 10

i = n
while i>0:
    n2 += (i%10)**dig
    i //= 10

if n == n2:
    print(n,"is a armstrong's number")
else:
    print(n,"is not a armstrong's number")