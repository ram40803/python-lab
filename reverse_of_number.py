n = int(input("enter a number:"))

rev = 0
i = n
while i>0:
    rev = rev*10 + i%10
    i //= 10

print(rev)