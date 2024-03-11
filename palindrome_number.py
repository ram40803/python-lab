n = int(input("enter a number:"))

rev = 0
i = n
while i>0:
    rev = rev*10 + i%10
    i //= 10

if rev == n:
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")