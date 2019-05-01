import string
list=list(string.ascii_lowercase)
n=int(input())
row=1
nst=1
nsp=(n*2)-2
while row<=(n*2)-1:
    ch=list[n-1]
    csp=1
    while csp<=nsp:
        print("-",end='')
        csp+=1
    cst=1
    while cst<=nst:
        if cst==nst:
            print(ch,end='')
        else:
            print(ch,end='-')
        if cst<=nst//2:
             ch=chr(ord(ch)-1)
        else:
            ch=chr(ord(ch)+1)
        cst+=1
    csp=1
    while csp<=nsp:
        print("-",end='')
        csp+=1
    print()
    if row<=((n*2)-1)/2:
        nst+=2
        nsp-=2
    else:
        nst-=2
        nsp+=2
    row+=1



