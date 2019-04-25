n=int(input())
list=[]
for i in range(n):
    a=[]
    a.append(input())
    a.append(input())
    list.append(a)
list.sort(key=lambda x:x[1])
for i in range(len(list)):
    if float(list[i][1]) !=float(list[i+1][1]):
        del list[i]
        break
print(list)
for j in range(len(list)):
    if float(list[j][1]) !=float(list[j+1][1]):
        print(list[j][0])
        break
    else:
        while float(list[j][1]) ==float(list[j+1][1]):
            for j in range(len(list)):
                if list[i][0]<list[i+1][0]:
                    print(list[i][0])
                    print(list[i+1][0])
                    break
                else:
                    print(list[i+1][0])
                    print(list[i][0])
                    break
            break        
    break