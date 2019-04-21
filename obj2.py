class Object():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def introduce(self):
        print("Values are %d and %d"%(self.a,self.b))
Object(1,2).introduce()