from tkinter import *

import mysql.connector
import sys
import config
from tkinter import ttk
import tkinter as tk
from RecipePage import RecipePage
from MealPage import MealPage
from ProfilePage import ProfilePage

usr = config.mysql['user']
pwd = config.mysql['password']
hst = config.mysql['host']
dab = 'asmith37_DB'
# create a connection
con = mysql.connector.connect(user=usr,password=pwd, host=hst, database=dab)
root = Tk()
root.title("Recipes")
root.geometry("900x600")


class LoginOrSignUp:
    """ The inital page of the program. This is where users can select if they want to log if __name__ == '__main__':
        to an existing account or create a new account """
    myFrame = None
    root = None

    def __init__(self, master):
        self.myFrame = Frame(master)
        self.myFrame.pack()
        self.root = master

        loginButton = ttk.Button(self.myFrame, text="Login with Existing Account", command=self.login).pack()
        createAccButton = ttk.Button(self.myFrame, text="Create Account", command=self.signup).pack()
        skipButton = ttk.Button(self.myFrame, text="Skip", command=self.skip).pack()


    def login(self):
        self.myFrame.destroy()
        print("logging in")
        l = Login(self.root)

    def signup(self):
        self.myFrame.destroy()
        s = SignUp(self.root)

    def skip(self):
        self.myFrame.destroy()
        m = MainProgram(root, "chef_anna0")


class Login:
    """ The login page. This allows users to enter their existing username and password. If they
    enter an incorrect username or password, they will be prompted to try again."""
    myFrame = None
    loginLabel = None
    root = None
    username = None
    password = None
    error = None

    # master refers to root
    def __init__(self, master):
        self.myFrame = Frame(master)
        self.myFrame.pack()
        self.root = master

        self.loginLabel = ttk.Label(self.myFrame, text="Login")
        self.loginLabel.grid(column=2, row=1, columnspan=2)

        usernameLabel = ttk.Label(self.myFrame, text="Username")
        usernameLabel.grid(column=2, row=2)

        self.username = StringVar()
        usr = ttk.Entry(self.myFrame, textvariable=self.username)
        usr.grid(column = 3, row=2)

        passwordLabel = ttk.Label(self.myFrame, text="Password")
        passwordLabel.grid(column=2, row=3)

        self.password = StringVar()
        pw = ttk.Entry(self.myFrame, textvariable=self.password)
        pw.grid(column = 3, row=3)

        loginButton = ttk.Button(self.myFrame, text="Login", command=self.login).grid(column=2, row=4, columnspan = 2, sticky=(W,E))

        #self.myButton = Button(self.myFrame, text="Click Me!", command=self.clicker)
        #self.myButton.pack()

    def login(self):
        loginUsername = self.username.get()
        loginPassword = self.password.get()
        print(loginUsername)
        print(loginPassword)
        rs = con.cursor()
        getPassword = '''SELECT password
                    FROM User
                    WHERE username = "%s"'''

        rs.execute(getPassword % (loginUsername))
        row = rs.fetchone()
        if row is not None:
            print(row[0])
            if (row[0] == loginPassword):
                print("login successful")
                self.myFrame.destroy()
                m = MainProgram(self.root, loginUsername)

        self.error = Tk()
        self.error.title("Error")
        self.error.geometry("250x150")

        messageLabel = ttk.Label(self.error, text="Invalid Username or Password")
        messageLabel.grid(column=1, row=1, columnspan=2)

        option1 = ttk.Button(self.error, text="Create Account", command = self.signUp)
        option1.grid(column=1, row=2)

        option2 = ttk.Button(self.error, text="Try Again", command = self.tryAgain)
        option2.grid(column=2, row=2)

    def signUp(self):
        self.error.destroy()
        self.myFrame.destroy()
        s = SignUp(root)

    def tryAgain(self):
        self.error.destroy()

class SignUp:
    """ This is the sign up page where users can create a new account. If the username
    they entered already exists in the database, they are prompted to try again"""
    myFrame = None
    signUpLabel = None
    root = None
    username = None
    password = None
    name = None

    # master refers to root
    def __init__(self, master):
        self.myFrame = Frame(master)
        self.myFrame.pack()
        self.root = master

        self.signUpLabel = ttk.Label(self.myFrame, text="Sign Up")
        self.signUpLabel.grid(column=2, row=1, columnspan=2)

        nameLabel = ttk.Label(self.myFrame, text="Name")
        nameLabel.grid(column=2, row=2)

        self.name = StringVar()
        nm = ttk.Entry(self.myFrame, textvariable=self.username)
        nm.grid(column = 3, row=2)

        usernameLabel = ttk.Label(self.myFrame, text="Username")
        usernameLabel.grid(column=2, row=3)

        self.username = StringVar()
        usr = ttk.Entry(self.myFrame, textvariable=self.username)
        usr.grid(column = 3, row=3)

        passwordLabel = ttk.Label(self.myFrame, text="Password")
        passwordLabel.grid(column=2, row=4)

        self.password = StringVar()
        pw = ttk.Entry(self.myFrame, textvariable=self.password)
        pw.grid(column = 3, row=4)

        loginButton = ttk.Button(self.myFrame, text="Sign Up", command=self.signUp).grid(column=2, row=5, columnspan = 2, sticky=(W,E))



    def signUp(self):
        signUpUsername = self.username.get()
        signUpPassword = self.password.get()
        rs = con.cursor()
        getPassword = '''SELECT password
                    FROM User
                    WHERE username = "%s"'''

        rs.execute(getPassword % (signUpUsername))
        row = rs.fetchone()
        if row is not None:
            self.error = Tk()
            self.error.title("Error")
            self.error.geometry("250x150")

            messageLabel = ttk.Label(self.error, text="Username Already Exists")
            messageLabel.grid(column=1, row=1, columnspan=2)

            option1 = ttk.Button(self.error, text="Create Account", command = self.signUp)
            option1.grid(column=1, row=2)

            option2 = ttk.Button(self.error, text="Try Again", command = self.tryAgain)
            option2.grid(column=2, row=2)

        else:
            print("create account")#query = '''INSERT INTO Users()
            self.myFrame.destroy()
            m = MainProgram(self.root, signUpUsername)

    def signUp(self):
        self.error.destroy()
        self.myFrame.destroy()
        s = SignUp(root)

    def tryAgain(self):
        self.error.destroy()

class MainProgram:
    currentUser = None
    myFrame = None
    root = None

    def __init__(self, master, user):
        self.myFrame = Frame(master)
        self.myFrame.pack()
        self.currentUser = user
        self.root = master

        my_notebook = ttk.Notebook(self.myFrame)
        my_notebook.pack()

        recipeFrame = Frame(my_notebook, width= 900, height = 600)
        mealSearchFrame = Frame(my_notebook, width= 900, height = 600)
        profileFrame = Frame(my_notebook, width= 900, height = 600)

        recipeFrame.pack(fill = "both", expand = 1)
        mealSearchFrame.pack(fill = "both", expand = 1)
        profileFrame.pack(fill = "both", expand = 1)

        my_notebook.add(recipeFrame, text = "Recipe Search")
        my_notebook.add(mealSearchFrame, text = "Meal Search")
        my_notebook.add(profileFrame, text = "Profile")

        r = RecipePage(recipeFrame, self.currentUser)
        m = MealPage(mealSearchFrame, self.currentUser)
        p = ProfilePage(profileFrame, self.currentUser)


l = LoginOrSignUp(root)
root.mainloop()
