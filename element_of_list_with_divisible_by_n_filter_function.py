n = int(input("enter a number:"))
l = [1,2,3,4,5,6,7,8,9]

ans = list(filter(lambda x:x%n==0,l))
print(ans)