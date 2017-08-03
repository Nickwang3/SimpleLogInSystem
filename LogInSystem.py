from tkinter import *
import json
import os
root = Tk()

logIns = {}
logIns['default']='default'

b = os.path.getsize("storage.json")  ##program does not run if storage is empty -- checks file size and if 0 adds default
if b == 0:
    with open("storage.json", 'w') as testfile:
        json.dump(logIns, testfile)
    testfile.close()

with open("storage.json", 'r') as infile:
     logIns = json.load(infile)
infile.close()

class LogInSystem(object):

    userName = ""
    passWord = ""



    def __init__(self, master):
        self.usernameL = Label(root, text="username")
        self.passwordL = Label(root, text="password")
        self.usernameE = Entry(root)
        self.passwordE = Entry(root, show="*")

        self.usernameL.grid(row=0, sticky=E)
        self.passwordL.grid(row=1, sticky=E)
        self.usernameE.grid(row=0, column=1)
        self.passwordE.grid(row = 1, column=1)

        self.c = Checkbutton(root, text="Keep me logged in")
        self.c.grid(columnspan=2)

        self.registerB = Button(root, text="Register New Account", command=self.register, fg="blue")
        self.registerB.grid(row=4, columnspan=2)

        self.logInB = Button(root, text = "Log in", command=self.logInAccepted, fg="green")
        self.logInB.grid(row=3, columnspan=2)



    def logInAccepted(self):
        userNameEntered = self.usernameE.get()
        passWordEntered = self.passwordE.get()

        print(userNameEntered)
        print(passWordEntered)

        # if (userNameEntered, passWordEntered) in logIns.items():
        #     print("Logging in")
        if userNameEntered in logIns and logIns[userNameEntered][0]==passWordEntered:
            print("Logging in")
        else:
            print("No account with that combination of username and password exists")
            print(logIns)



    def register(self):
        print("Registering new username and password...")
        userName = self.usernameE.get()
        passWord = self.passwordE.get()



        print(userName)
        print(passWord)

        logIns[userName] = [passWord]

        with open("storage.json", 'w') as outfile:
            json.dump(logIns, outfile)
        outfile.close()





logIn1 = LogInSystem(root)


root.mainloop()
