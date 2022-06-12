def greeting_user():
    print("Hello users")
    print("Welcome to world .K xa guys")

print("start")
greeting_user()
print("finish")

#program2
def greeting_user(name):
    print(f"Hello {name}")
    print("Welcome to world .K xa guys")

print("start")
greeting_user("samir")
greeting_user("bishal")
print("finish")

#program3: parameter
def greeting_user(first_name,last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome to world .K xa guys")

print("start")
greeting_user("samir","Kc")
greeting_user("bishal","Kc")
print("finish")

#program 4 : Keyword argument
def greeting_user(first_name,last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome to world .K xa guys")

print("start")
greeting_user(last_name="samir",first_name="Kc")
greeting_user(last_name="bishal",first_name="Kc")
print("finish")
