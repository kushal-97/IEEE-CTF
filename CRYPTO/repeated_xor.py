def rep_xor(str1,str2):
    l1=len(str1)
    l2=len(str2)
    n=[]
    if l1<l2:
        l=l1
    else:
        l=l2
    for i in range(0,l):
        x1=int(str1[i],16)
        x2=int(str2[i],16)
        n.append(hex(x1^x2))
    print(''.join(n))
    
    
