l = [1,2,3,4,3,5,2]

i = 0
l2 = []
for x in l:
    if x not in l2:
        l2.append(x)

print(l2)