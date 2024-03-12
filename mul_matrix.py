n = int(input("enter order of matrix:"))

def inputMatrix(n):
    m = []
    print("enter elements of Matrix:")
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(int(input(f"element {i},{j}:")))
    return m

def displayMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end=" ")
        print()

def mulMatrix(m1,m2):
    m = []
    for i in range(len(m1)):
        m.append([])
        for j in range(len(m2[0])):
            e = 0
            for k in range(len(m1)):
                e += m1[i][k]*m2[k][j]
            m[i].append(e)
    return m

m1 = inputMatrix(n)
print()
m2 = inputMatrix(n)
m = mulMatrix(m1,m2)
print()
print("result:")
displayMatrix(m)
