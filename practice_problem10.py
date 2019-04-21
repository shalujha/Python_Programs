n=int(input())
power=1
decimal=0
while n!=0:
    r=n%10
    decimal+=r*power
    power*=2
    n//=10
print(decimal)


