#Ask the user for his name then confirm that he has entered his
#name(not an empty string/integers). then proceed to ask him for
#his email and print all this data (Bonus) check if it is a valid email
#or not

def nameOfUser():
     x = input()
     fname= input("PLz enter your firstname :")
     lname= input("PLz enter your lastname :")
     Email= input("Plz enter your valid email:")

     if x !=None:
      print(x)
     else:

      print("empty input")

     return fname, lname, Email


res=nameOfUser()
print(res)
print(type(res))