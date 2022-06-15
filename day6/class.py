class Person:
    def __init__(self,fname,lname):
          self.firstname=fname
          self.lastname=lname
    def printname(self):
         print("The name is " + self.firstname , self.lastname)
p1=Person("Samir","KC")
p1.printname()
