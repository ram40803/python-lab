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

def transpose(m):
    for i in range(len(m)):
        for j in range(i):
            temp = m[j][i]
            m[j][i] = m[i][j]
            m[i][j] = temp
 
m = inputMatrix(n)
displayMatrix(m)
transpose(m)
print("")
displayMatrix(m)