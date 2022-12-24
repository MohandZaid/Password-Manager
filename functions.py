import re
import time
import random
import hashlib

from database import *

# To-Do : add uniqe email checker in registiration
# To-Do : check valid real date 


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

    matched = re.search(pattern,input_from_user)
    if matched :
        return True
    return False

def is_strong_password(password):

    # Check length (minimum 8 characters)
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase, one lowercase letter, and one digit
    if not re.search(r'[A-Z]', password) or \
       not re.search(r'[a-z]', password) or \
       not re.search(r'\d', password):

        return False
    
    # Check for at least one special character (!@#$%^&*)
    if not re.search(r'[!@#$%^&*]', password):
        return False
    
    return True

def hash_password(password):

    # Convert password string to bytes
    password_bytes = password.encode('utf-8')

    # Create SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the password bytes
    sha256_hash.update(password_bytes)

    # Get the hexadecimal representation of the hash
    hashed_password = sha256_hash.hexdigest()

    return hashed_password


# To-Do: Make all interaction with user in prompt script
# To-Do: Pass all needed variables from prompt to this func as arguments
def make_profile(username, email, master_password, confirm_pass):

    if not check_valid(username, 'username'):
        return 'false_username'

    if not check_valid(email, 'email') :
        return 'false_email'

    if not is_strong_password(master_password) :
        return 'weak_password'

    if not master_password == confirm_pass :
        return False
    
    master_password = hash_password(master_password)

    return { 'username': username , 'email': email, 'master_password': master_password } 


def password_gen(length=10):

    # Define the characters to use in the password
    # Avoided characters : \<>|~
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV\
WXYZ0123456789!#$%&*+-_./:;=?@'

    # Generate a password with random characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

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


def enter_profile(username, password, debug=False):
    if debug :
        debugger = ('user@debug.com', 'debug')
        return debugger

    if username in DBHandler.get_all_profile_names() :
        
        if password == DBHandler.get_password(username=username) :
            return True
        return False

    return 'not-user'

