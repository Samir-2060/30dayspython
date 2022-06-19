import random

roll=True

while roll:
  print(random.randint(1,6))
  another_roll=input("want to roll dice again ? (Y/N):")
  if another_roll.lower()=="y":
        continue
   else:
      break
