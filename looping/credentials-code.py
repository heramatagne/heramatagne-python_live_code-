#This program contains a code that first asks a user for a username and password.
# Then, checks for the username and password validity. If correct it will grant access to user.
# If not it will ask the user to enter their password or username 5 times. 
# After 5 attempts,  the account would be locked.
print('Enter your username and password to continue')
count = 0

# initializing by using "" or '' to assign a value string into it
password = ""
username = ""

# looping will continue when wrong input for five times and ask again, and would locked the account.
while username!='hdsm' and password!='smile' and count < 5:
    # collect user input from CLI separately.
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username=='hdsm' and password=='smile':
     # if match, grand and break
     print('You have access!')
     break
    else:
        count+=1
        print('Enter your username or your password.')
        # after 5 attempts account will be locked.
        if count == 5:
            print('Account locked.')
    
