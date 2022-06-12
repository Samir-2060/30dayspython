class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        print("draw")
    def move(self):
        print("move")
point1=Point(10,15)
print(point1.x)
print(point1.y)

#program 2
class Person:
    def talk(self):
        print("talk")
bishal=Person()
bishal.talk()

#program3
class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print("talk")
name2=Person("samir")
print(name2.name)
name2.talk()

#program4
class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi I am a {self.name}")
name2=Person("samir")
name2.talk()
