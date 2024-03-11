n = int(input("enter order of matrix:"))

def inputMatrix(n):
    m = []
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

def addMatrix(m1,m2):
    if(len(m1) == len(m2)):
        m = []
        for i in range(len(m1)):
            m.append([])
            for j in range(len(m2)):
                m[i].append(m1[i][j]+m2[i][j])
        return m

m1 = inputMatrix(n)
m2 = inputMatrix(n)
m = addMatrix(m1,m2)
displayMatrix(m)