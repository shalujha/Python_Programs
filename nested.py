list=[]
n=int(input())
for i in range(n):
   student=[input(),float(input())]
   list.append(student)
list.sort(key=lambda x:x[1])
#print(list)
second_largest=list[0][1]
for j in range(1,len(list)):
    if second_largest<list[j][1]:
        second_largest=list[j][1]
        break
#print(second_largest)
for c in sorted(list):
    if c[1]==second_largest:
        print(c[0])