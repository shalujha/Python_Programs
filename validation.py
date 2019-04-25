t=int(input())
for i in range(t):
    n=input()
    if n.isalnum()==False:
        print("Invalid")
    else:
        if len(n)==10:
            indicator=0
            digits=0
            characters=0
            for j in range(len(n)):
                for k in range(j+1,len(n)):
                    if n[j]==n[k]:
                        indicator=1
                        break
                if indicator==1:
                    print("Invalid")
                    break
            if indicator==0: 
                for c in n:
                    if c.isdigit():
                        digits+=1
                    if c.isupper():
                        characters+=1
            if digits>=3 and characters>=2:
                print("Valid")
        else:
            print("Invalid")        

