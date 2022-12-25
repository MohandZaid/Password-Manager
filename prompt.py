import os , sys

from termcolor import colored
from getpass import getpass

from functions import *
from database import *
from secretscrypto import *


banner = '''
     ____                  __  ___                
    / __ \____  ____ _____/  |/  /___  ____  _____
   / /_/ / __ `/ ___` ___/ /|_/ / __ \/ __ \/ ___/
  / ____/ /_/.(__  |__  ) /  / / / / / /_/ / /    
 /_/    \__,_/____/____/_/  /_/_/ /_/\__, /_/     
                  By`Mohand Zaid`/_______/        

                '''

dev = ' Developed By: Mohand Zaid (mohandzaid33@gmail.com)'
help_msg = ' (h)help to show commands!'
 

class Prompt :

    def __init__(self, prompter='PassMngr > ', color=False) :
        self.prompter = prompter
        self.colored = color

        if self.colored :
            print(colored(banner,'yellow'))
        else:
            print(banner)
            print("Colored Mode Off\nrun 'pip install pyfiglet termcolor'and restart program\n")

        while True :

            if self.colored :
                main_prompt = input(colored(f'\n{self.prompter}', 'yellow')).lower().strip()
            else :
                main_prompt = input(f'\n{self.prompter}').lower().strip()

            if self.general_commands(main_prompt) is False :
                if self.main_prompt_commands(main_prompt) is False :
                    print('Command Not Found')


    def mkpf_action(self):

        username = input('Username : ').lower().strip()
        email = input('Email : ').lower()
        master_password = getpass('Password : ').strip()
        confirm_pass = getpass('Confirm-Password : ').strip()

        if username in DBHandler.get_all_profile_names():
            print('\nAlert: Username Already Exist')
            return

        pf_data = make_profile(username, email, master_password, confirm_pass)

        if pf_data == 'false_username' :
            print('\nAlert: Invalid Username')

        if pf_data == 'false_email' :
            print('\nAlert: Invalid Email')
        
        if pf_data == 'weak_password' :
            print('\nAlert: Weak Password')
            print("Please ensure your password meets the following criteria:")
            print("- At least 8 characters long")
            print("- Includes at least one uppercase letter, one lowercase letter, one digit")
            print("- Includes at least one special character (!@#$%^&*)")

        elif pf_data :
            print('\nProfile Added Successfully')
            DBHandler(pf_data['username'], pf_data['master_password'], pf_data['email'])

        return 

    def enter_action(self):

        username = input('Username : ').lower().strip()
        master_password = hash_secret(getpass('Password : ').lower().strip())

        if enter_profile(username, master_password) :
            UserPrompt(user=username, prompter=f'{username} > ', color=self.colored)

    def help_msg(self) :
        print("\n- (mkpf) make-profile\n- (enter) enter-profile\n- (sec) prompt-secret\n\
- (h) help\n- (i) info\n- (c) clear\n- (e) exit\n- (re) restart")
        

    def general_commands(self, command):
        
        if command == '' :
            return

        elif command in ['help', 'h'] :
            self.help_msg()
        
        elif command in ['info', 'i'] :
            print(banner)
            print(dev)
            print(help_msg)
    

        elif command in ['clear', 'c'] :
            os.system('clear')
 
        elif command in ['e', 'exit'] :
            sys.exit()
       
        elif command in ['restart', 're'] :
            self.restart()

        else :
            return False


    def main_prompt_commands(self, command):

        if command == '':
            return

        elif command in ['make-profile', 'mkpf'] :

            try:
                self.mkpf_action()

            except KeyboardInterrupt:
                pass

        elif command in ['enter-profile', 'enter'] :
            
            try:
                self.enter_action()

            except KeyboardInterrupt:
                pass

        elif command in ['d', 'debug'] :
            try:
                UserPrompt('test', color=True)
            except KeyboardInterrupt:
                pass

        elif command in ['create-secret', 'sec'] :
            print(f'\n{password_gen()}')


        else:
            return False
        
    def restart(self):
        
        print("\nRestarting PassMngr ...\n")
        app = sys.executable
        os.execl(app, app, *sys.argv)


class UserPrompt(Prompt) :

    def __init__(self, user, prompter='user > ', color=False):

        self.user = user
        self.prompter = prompter
        self.colored = color

        self.prompter = f'{self.user}@PassMngr > '

        while True :

            if self.colored :
                main_prompt = input(colored(f'\n{self.prompter}', 'yellow')).lower().strip()
            else :
                main_prompt = input(f'\n{self.prompter}').lower().strip()
            
            if self.general_commands(main_prompt) is False :
                if self.user_commands(main_prompt) is False :
                    print('Command Not Found')

    
    def create_secret(self):
            website = input('Website : ').lower().strip()

            email = input('Email : ').lower().strip()
            if not check_valid(email, 'email') :
                print('\nAlert: Invalid Email')
                return

            password = password_gen()

            print(password)

            password = encrypt_secret(DBHandler.get_password(self.user), password)

            start = password_status('start')
            expiry = password_status('setexpiry')

            return {website : {'email': email, 'password': password,\
                            'start': start, 'expiry': expiry}}

    def help_msg(self) :
        print("\n- (sec) create-secret\n- (h) help\n- (i) info\n- (c) clear\n\
- (e) exit\n- (re) restart")

    def user_commands(self, command) :

        if command in ['test'] :
            print('test')
     
        elif command in ['create-secret', 'sec'] :
            print(self.create_secret())


        else :
            return False
        
