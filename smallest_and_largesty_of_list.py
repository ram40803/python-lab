l = [1,523,1234,3,5,1]

s = la = l[0] if len(l)>0 else None
for x in l:
    if(x>la):
        la = x
    if(x<s):
        s = x

print("smallest element is",s)
print("largest element is",la)