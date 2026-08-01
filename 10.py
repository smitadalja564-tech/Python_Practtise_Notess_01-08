db ={
    "username ": '',
    "email" : '',
    "password" : '' ,
}
menu = """
           Menu

           [ 1 ] Press 1 for registartion
           [ 2 ] Press 2 for login
"""
def login():
    print("Sign In Page Here...")
    email = input("Enter Your Email : ").lower()
    password = input("Enter Your Paswword : ").lower()

    if email == db["email"] and password == db["password"]:
        return f"welcome {db['username']},"
    elif email != db["email"] or  password != db["password"]:
        return f"Inavlid email or password"
    else:
        return f"Please check your registration Status...!"

def registration():
    print("Sign Up Page Here.....")
    username = input("Enter Username : ")
    email = input("Enter Email : ")
    password = input("Enter Password : ")

    if username in db.keys():
        print("Alrady Registered..!")
    else:
        db['username'] = username
        db['email'] = email
        db['password'] = password
status = True

while status:
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        registration()
    elif choice == 2:
        print(login())
    
    continue_choice = input("Do you want to continue press 'y' for yes and 'n' for no : ").lower()
    if continue_choice == 'y' or continue_choice == 'yes':
        status = True
    else:
        status = False
