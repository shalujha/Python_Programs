# By default all the class variables are public in nature
# we can make a method or variable private by using double underscore and if u make a method private , u cant use it directly
# either class can use this private method or u have to call any method of class to execute that method
# Instance Variables vs Class Variables
class Dog():
    color="Brown"
    # this list is common for all data members of class, to resolve this we will add the values in different constructors
    def __init__(self , breed):
        """This method accepts the breed of the dog and initialises it"""
        self.breed=breed
        self.activities=[]
    def addActivity(self,act): # public method
        self.activities.append(act)
    def __SecretActivity(self):  # private method
        print("Doing Secret Activity"+self.breed)
    def doActivities(self): # public method
        print(self.activities)
        print(self.breed)
        self.__SecretActivity()
  
d1=Dog("German Stephard")
d2=Dog("Golden Retriever")
d1.addActivity("High Jump")
d1.addActivity("Roll First")
d2.addActivity("High Jump")
d2.addActivity("Roll First")
# d1.SecretActivity()
# d2.SecretActivity()
d1.doActivities()
d2.doActivities()
