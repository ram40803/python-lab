for i in range(500,1000):
    rev = 0
    j = i
    while j>0:
        rev = rev*10 + j%10
        j //= 10

    if rev == i:
        print(i,end=" ")