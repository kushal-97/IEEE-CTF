def xor(str1,str2):
    l1=len(str1)
    l2=len(str2)
    n=[]
    if l1<l2:
        l=l1
    else:
        l=l2
    for i in range(0,l):
        x=chr(ord(str1[i])^ord(str2[i]))
        n.append(x)
    print(''.join(n))    
                  
