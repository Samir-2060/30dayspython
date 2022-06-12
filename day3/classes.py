class Point:
    def draw(self):
        print("draw")
    def move(self):
        print("move")
point1=Point()
point1.draw()
point1.move()
point1.x=10
point1.y=20
print(point1.x)
print(point1.y)
#two objects of class Point are totally different from each other.
point2=Point()
point2.x=50
print(point2.x)
