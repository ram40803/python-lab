n = int(input("enter a number:"))

def ispalindrome(n):
    rev = 0
    i = n
    while i>0:
        rev = rev*10 + i%10
        i //= 10
    if rev == n:
        return True
    else:
        return False

if ispalindrome(n):
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")