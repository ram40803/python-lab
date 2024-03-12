l = [3,4,6,7]

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        print("list is not sorted")
        break
else:
    print("list is sorted")