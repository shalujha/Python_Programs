str=input()
k=int(input())
list=[]
i=0
while i!=len(str):
    list.append(str[i:i+k])
    i+=k
ans=[]
def removeDuplicates(string):
    p=''
    for i in range(len(string)):
        if string[i] not in p:
            p+=string[i]
    return p

for j in range(len(list)):
    ans.append(removeDuplicates(list[j]))
for k in range(len(ans)):
    print(ans[k])
