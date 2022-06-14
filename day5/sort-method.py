#sort method is used to sort the list element.Can be used to arrange the list in ascending order or descending order.By defaul it sort in ascending.
#program1
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)


#program2
#descending
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)

#beside this we can use sort method also to sort the list by the length of value.

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)
