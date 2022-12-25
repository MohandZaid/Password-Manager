import re
import time
import random

from database import *
from secretscrypto import *

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

def make_profile(username, email, master_password, confirm_pass):

    if not check_valid(username, 'username'):
        return 'false_username'

    if not check_valid(email, 'email') :
        return 'false_email'

    if not is_strong_password(master_password) :
        return 'weak_password'

    if not master_password == confirm_pass :
        return False
    
    master_password = hash_secret(master_password)

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

def enter_profile(username, password):

    if username in DBHandler.get_all_profile_names() :
        
        if password == DBHandler.get_password(username=username) :
            return True
        return False

    return 'not-user'

