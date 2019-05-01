N,m=map(int,input().split(" "))
c='.|.'
for i in range(1,N,2):
    print((c*i).center(m,'-'))
print("WELCOME".center(m,'-'))
for j in range(N-2,-1,-2):
    print((c*j).center(m,'-'))