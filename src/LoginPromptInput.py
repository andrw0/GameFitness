import sys

CorrectUsername = "testusername"
CorrectPassword = "testpassword"

loop = 'true'
while (loop == 'true'):
    username = raw_input("Please enter your username: ")
    if (username == CorrectUsername):
    	password = raw_input("Please enter your password: ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Password incorrect!"
    else:
        print "Username incorrect!"
