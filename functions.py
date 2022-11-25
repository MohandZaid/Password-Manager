import re
import time
import random


# To-Do : add uniqe email checker in registiration
# To-Do : check valid real date 
# To-Do: Check Strong Password


def id_gen():
    current_time = int(time.time())
    random_number = random.randint(0, 9999)
    
    return f"{current_time}{random_number}"

def check_valid(input_from_user, check):

    if not check :
        return 'Check label not detected.'
    elif check == 'email' :
        pattern = r'^[\w\d\._-]+@[\w\d\.-]+\.[\w]{2,}$'

    elif check == 'date' :
        pattern = r'\d{1,2}-\d{1,2}-\d{4}'

    elif check == 'username' :
        if not input_from_user.isalpha() :
            return False
        return True

    elif check == 'string' :
        return all(i.isalpha() or i.isspace() for i in input_from_user)

    #To-Do: Check Strong Password
    elif check == 'passwrod':
        pass


    matched = re.search(pattern,input_from_user)
    if matched :
        return True
    return False

def make_hash(password):
    pass

# To-Do: Make all interaction with user in prompt script
# To-Do: Pass all needed variables from prompt to this func as arguments
def make_profile(username, email, master_password, confirm_pass):

    if not check_valid(username, 'username'):
        return 'false_username'

    if not check_valid(email, 'email') :
        return 'false_email'

    # To-Do: check password strength
    # if not check_valid(master_password, 'password'):
        # return 'weak_password'

    if not master_password == confirm_pass :
        return False
    
    master_password = make_hash(master_password)

    return { 'username': username , 'email': email, 'master_password': master_password } 


def password_gen():
    pass

# This function to manage password expiration
def password_status(query):
    pass


# To-Do: Make all interaction with user in prompt script
# To-Do: Pass all needed variables from prompt to this func as arguments
def secret_templet():

    # To-Do: Check valid domain name
    website = input('Website : ').lower().strip()

    email = input('Email : ').lower().strip()
    if not check_valid(email, 'email') :
        return 'false_email'

    password = password_gen()

    start = password_status('start')
    expiry = password_status('setexpiry')

    return {website : {'email': email, 'password': password,\
                       'start': start, 'expiry': expiry}}


# To-Do: Make function to fetch profiles database
global users, profiles

def login(username, password, debug=False):
    if debug :
        debugger = ('user@debug.com', 'debug')
        return debugger

    if username in profiles :
        
        user = profiles[username]

        if make_hash(password) == user['password'] :
            return True
        return False

    return 'not-user'

