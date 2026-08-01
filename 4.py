session = {
    'is_login' : False,
    "email" : ""
}

user_email = "delu20@gmail.com"
user_password = "d102003"

def login():
    email = input("Enter Your Email Address : ")
    password = input("Enter Your Password : ")

    if email == user_email and password == user_password:
        session["is_login"] = True
        session["email"] = email
    else:
        print("Invalid Credrentials..!!")
    
def auth(myfun):
    def wrapper():
        if session["is_login"]:
            myfun()
        else:
            print("Authentical Denied !! Please Login First")
    return wrapper

@auth
def deshbord():
    print("Welcome To Dashbord..!")

@auth
def profile():
    print("Welcome To User Profile..!")

@auth
def logout():
    session["is_login"] = False
    session["email"] = ""

menu = """"
            Press 1 -> Login
            Press 2 -> Dashbord
            Press 3 -> Profile
            Press 4 -> account
            Press 5 -> logout
"""

status = True
while status:
    print(menu)

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        login()
    elif choice == 2:
        deshbord()
    elif choice == 3:
        profile()
    elif choice == 4:
        pass
    elif choice == 5:
        logout()