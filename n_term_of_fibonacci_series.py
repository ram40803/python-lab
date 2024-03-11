n = int(input("enter number of terms:"))

a = 0
b = 1
for i in range(n):
    print(a,end=" ")
    a = a + b
    b = a - b