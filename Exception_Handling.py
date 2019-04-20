# error ocuurs while execution of program is called Exception and handling those errors to prevent the 
# abrupt termination is called Exception Handling
# Try and Except
# Exception is an inbuilt class in Python
try:
    # a=10/0
    # a=b
    # f=open("Something_missing.txt",'r')
    a=input("enter your name")
    if len(a)<3:
        raise Exception
except FileNotFoundError:
    print("file doesnt Exists!! Please reupload")
except NameError: # Specific Exception
    print("b is not defined")
    print(NameError)
except Exception: # generalised Exception
   # print("Something Went Wrong")
   print("Enter Valid name")
   # print(Exception)
else:
    print("try block executed without any error")
    print("Form Submitted Successfully")
finally:
    print("It is always there")