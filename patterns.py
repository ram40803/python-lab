n = int(input("enter a number:"))

for i in range(n):
    for j in range(i+1):
        print(end="*")
    print()
print()

for i in range(n):
    for j in range(n-i):
        print(end="*")
    print()
print()

for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for j in range(2*i+1):
        print(end="*")
    print()
print()

for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
print()

print("pascal's triangle")
