n = int(input("enter a number:"))

print("by list compreshension")
l = [x*10 for x in range(1,n+1)]
print(l)

print("by lambda function")
l2 = list(map(lambda x:x*10,range(1,n+1)))
print(l2)