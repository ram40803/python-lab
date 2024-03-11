n = int(input("enter a number:"))

sum = 0
i = n
while i>0:
    sum += i%10
    i //= 10

print(sum)