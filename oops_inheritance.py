# basically used for code resuability
# there is a is-a relationship between parent and child class
class SchoolMember():  # base Class
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Init School member: %s"%(self.name))
    def introduce(self):
        print("Name is %s %d"%(self.name,self.age))
class Teacher(SchoolMember):      # derived class
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print("Init Teacher %s"%(self.name))
    def introduce(self):
        SchoolMember.introduce(self)
        print("salary is : %d"%(self.salary))
class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print("Init Student %s"%(self.name))
    def introduce(self):
        SchoolMember.introduce(self)
        print("Marks is %d"%(self.marks))

# t=Teacher("shalini",19,20000)
# t.introduce()
s=Student("shalini",19,100)
s.introduce()


