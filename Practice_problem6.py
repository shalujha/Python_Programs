class obj():
    def __init__(self,a=0,b=1):
        self.a=a
        self.b=b
if __name__=="__main__":
    objects=[obj(1,2),obj(5,4),obj(7,3),obj(11,42),obj(8,0),obj(5,9)]
list1=[]
list2=[]
for i in range(len(objects)):
    list1.append(objects[i].a)
    list2.append(objects[i].b)
print(sorted(list1))
print(sorted(list2))

    