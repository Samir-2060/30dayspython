#program1
import random
for i in range(3):
    print(random.randint(10,30))
    
  #program2
 import random
members=['bishal','samir','nirmal','chirungb']
random2=random.choice(members)
print(random2)


#program2
import random

class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second
dice=Dice()
print(dice.roll())
