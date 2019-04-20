# __name__=='__main__'
# concept is the module that has been executed directly will have name as main.
if(__name__=='__main__'):
    # specify the work when this module is executed directly
    print("Module is %s",(__name__))
else:
    # specify the work when this module is imported
    print("I m in Module1 else Block")
# this concept is used when there is a need to distinguish module that has been executed directly and indirectly
