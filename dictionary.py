n=int(input())
d={}
for i in range(n):
    name, number = input().split()
    d[name] = int(number)
# print(d)
while True:
    try:
        a=input()
        if a in d:
            print('{}={}'.format(a,d[a]))
        else:
            print("Not found")
    except:
        break    
