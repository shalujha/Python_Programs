# Instance Variables vs Class Variables
class Dog():
    color="Brown"
    # this list is common for all data members of class, to resolve this we will add the values in different constructors
    def __init__(self , breed):
        self.breed=breed
        self.activities=[]
    def addActivity(self,act):
        self.activities.append(act)
    def doActivities(self):
        print(self.activities)
        print(self.breed)
d1=Dog("German Stephard")
d2=Dog("Golden Retriever")
d1.addActivity("High Jump")
d1.addActivity("Roll First")
d2.addActivity("High Jump")
d2.addActivity("Roll First")

d1.doActivities()
d2.doActivities()