t=int(input())
for i in range(t):
    n=int(input())
    odd=0
    even=0
    while n != 0:
        r=n%10
        if r%2 == 0:
            even += r
        else:
            odd += r
        n //= 10
    if even%4 == 0 or odd%3 == 0:
        print("Yes")
    else:
        print("No")
        
