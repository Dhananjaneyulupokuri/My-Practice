def SampleFunction():
   a = 1500
   print(type(a))
   return a
SampleFunction()
SampleFunction()
SampleFunction()
SampleFunction()

def is_stronger_password(password):
    if(len(password) < 8):
       return False
    if not any (char.isdigit() for char in password):
         return False   
    if not any (char.islower() for char in password):
         return False
    if not any (char.isupper() for char in password):
         return False
    if not any(char in '@#$%^&+=-_' for char in password):
         return False
    return True
print(is_stronger_password("Password123!"))
print(is_stronger_password("weakpass"))

def factorial(n):
    if n==0:
       return 1
    else:
       return n*factorial(n-1)
print(factorial(5)) 