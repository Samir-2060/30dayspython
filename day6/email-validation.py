
def validate(email):
    email = [char for char in email]
    at_counter = 0
    space_counter = 0
    dot_counter = 0
    invalid = False
    for character in range(len(email)):
        if email[character] == '@':
            at_counter += 1
        elif email[character] == ' ':
            space_counter += 1
        elif email[character] == '.':
            dot_counter += 1
        else:
            email[character] = email[character].lower()
               
    if at_counter != 1 or space_counter > 0 or dot_counter != 1 or (not email[0].isalpha()):
        print("Invalid email")
    else:
        return ''.join(email)
        
 
email = input("Enter the email: ")
print(validate(email))
