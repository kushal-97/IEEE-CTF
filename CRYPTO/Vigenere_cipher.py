def vig():
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    print(alpha)
    for i in range(1,26):
        x=alpha[0]
        del alpha[0]
        alpha.append(x)
        print(alpha)
    print('enter the plaintext')
    p=input()
    pt=p.upper()
    ptl=list(pt)
    k=input("enter the keyword-")
    key=k.upper()
    keyl=list(key)
    lp=len(ptl)
    lk=len(keyl)
    d=lp-lk
    if lp!=lk:
        if d>=lk:
            while d>=lk:
                keyl+=keyl
                d=d-lk
        if d<lk:
            for i in range(0,d):
                keyl.append(keyl[i])
        
            
    nk=keyl
    row=[]
    for j in range(0,lp):
        ak=ord(nk[j])          #ascii value of letter
        xp=ptl[j]              #plaintext letter
        ap=ord(xp)             #ascii value of plaintext letter
        dr=ak-65
        dc=ap-65
        diff=25-dc
        if dr<=diff:
            row.append(chr(ap+dr))
        else:
            s=dr-diff
            row.append(chr(64+s))
    
    print('in string form-',''.join(row))
    print('enter the new ciphertext')
    ct=input()
    print('enter new key')
    k=input()
    ctu=ct.upper()
    ku=k.upper()
    ctl=list(ctu)
    kl=list(ku)
    lc=len(ctl)
    lk=len(kl)
    d=lc-lk
    if lc!=lk:
        if d>=lk:
            while d>=lk:
                kl+=kl
                d=d-lk
        if d<lk:
            for i in range(0,d):
                kl.append(kl[i])
    
    pt=[]
    for i in range(0,lc):
        ac=ord(ctl[i])
        ak=ord(kl[i])
        
        if ak<=ac<=90:
            d=ac-ak
            pt.append(chr(65+d))
        else:
            d=ac-65
            di=90-ak
            diff=25-di
            
            pt.append(chr(91-(diff-d)))
    
             

    print('in form of string=',''.join(pt))
    





                      
