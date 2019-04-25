str=input()
max=0
for i in range(len(str)):
    count=0
    for j in range(1,len(str)):
        if str[i]==str[j]:
            count+=1
    if max<count:
        max=count
        maxCharacter=str[i]
print(maxCharacter)

