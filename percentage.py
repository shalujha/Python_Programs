n=int(input())
student={}
for i in range(n):
     name,*line=input().split() #* is for tuple and ** is for dictionary
     scores=list(map(float,line))
     student[name]=scores
#print(student)
query=input()
list=student[query]
print("%.2f"%(sum(list)/len(list)))


