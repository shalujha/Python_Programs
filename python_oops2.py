class Person():
    # class Variable : these variables are common for all the objects of same class
    nationality="Indian"
    def __init__(self,Pname,clg): # it is basically a constructor that is initialising object
        # Instance variables: these are different for every instance of same class
        self.name=Pname
        self.college=clg
    def sayHi(self,name): # self is basically a current class object
        print("Hello "+ name)
    def introduce(self):
        print("My name is "+self.name)
        print("college is "+ self.college)
        print("I m "+self.nationality)
p=Person("shalini","Mait")
p2=Person("Ayush","IIT")
p.sayHi("World")
p.introduce()
p2.introduce()