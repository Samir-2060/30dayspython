try:
    age=int(input("age:"))
    salary=5000
    risk =salary /age
    print (age)

except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print("Ivalid enter")
