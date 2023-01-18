import os , sys
from time import sleep
from getpass import getpass

try :
    from termcolor import colored
except ModuleNotFoundError :
    pass

from functions import *
from database import *
from secretscrypto import *
from banners import *


dev = 'Developed By: Mohand Zaid (mohandzaid33@gmail.com)'
help_msg = '(h)help to show commands!'
 

class Prompt :

    def __init__(self, prompter='PassMngr > ', color=False) :
        self.prompter = prompter
        self.colored = color

        if self.colored :
            print(colored(bannar_passmngr, self.colored))
            print(colored(dev, self.colored))
            print(colored(help_msg, self.colored))
        else:
            print(bannar_passmngr)
            print(dev)
            print("\nColored Mode Off\nrun 'pip install termcolor'and restart program\n")

        while True :

            if self.colored :
                main_prompt = input(colored(f'\n{self.prompter}', self.colored)).lower().strip()
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

        if username in\
            DBHandler.get_all_profile_names(db_to_query='profilesdb.json'):
            print('\nAlert: Username Already Exist')
            return

        pf_data = make_profile(username, email, master_password, confirm_pass)

        if pf_data == 'false_username' :
            print('\n(Alert) Invalid Username')

        if pf_data == 'false_email' :
            print('\n(Alert) Invalid Email')
        
        if pf_data == 'weak_password' :
            print(f'\n(Alert) Weak Password')
            print("Please ensure your password meets the following criteria:")
            print("- At least 8 characters long")
            print("- Includes at least one uppercase letter, one lowercase letter, one digit")
            print("- Includes at least one special character (!@#$%^&*)")
        
        if pf_data == 'not_match' :
            print('\n(Alert) Password Not Match')

        elif isinstance(pf_data, dict) :
            print('\n(Successful) Profile Added')
            DBHandler(pf_data['username'], pf_data['master_password'],\
                    pf_data['email'])

        return 

    def enter_action(self):

        username = input('Username : ').lower().strip()
        master_password = getpass('Password : ').strip()

        enter = enter_profile(username, master_password)
        if enter == 'not-user':
            print(f'\n(Alert) Invalid Profile')

        elif enter[0] is True :
            print(f'\n(Successful) Entery')
            UserPrompt(user=username, prompter=f'{username} > ', color=self.colored, key=enter[1])
        else :
            print(f'\n(Alert) Invalid Password')

    def help_msg(self) :
        print("\n- (mkpf) make-profile\n- (enter) enter-profile\n- (sec) prompt-secret\n\
- (h) help\n- (i) info\n- (c) clear\n- (e) exit\n- (re) restart")
        

    def general_commands(self, command):
        
        if command == '' :
            return

        elif command in ['help', 'h'] :
            self.help_msg()
        
        elif command in ['info', 'i'] :
            print(bannar_passmngr)
            print(dev)
            print(help_msg)
    

        elif command in ['clear', 'c'] :
            os.system('cls' if os.name == 'nt' else 'clear')
 
        elif command in ['e', 'exit'] :
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.colored :
                print(colored(bannar_passmngr, self.colored))
                print(colored(bannar_lock, self.colored))
            else :
                print(bannar_passmngr)
                print(bannar_lock)

            sys.exit()
       
        elif command in ['restart', 're'] :
            os.system('cls' if os.name == 'nt' else 'clear')
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
                UserPrompt('test', color=self.colored)
            except KeyboardInterrupt:
                pass

        elif command in ['create-secret', 'sec'] :
            print(f'\n(Generated-Secret) {password_gen()}')


        else:
            return False
        
    def restart(self):

        print("\nRestarting PassMngr ...\n")
        app = sys.executable

        if os.name == 'nt' :
            subprocess.call([app] + sys.argv)
        else:
            os.execl(app, app, *sys.argv)


class UserPrompt(Prompt) :

    def __init__(self, user, prompter='user > ', color=False, key=''):

        self.user = user
        self.prompter = prompter
        self.colored = color
        self.key = key

        self.prompter = f'{self.user}@PassMngr > '

        if self.colored :
            print(colored(bannar_open_lock, self.colored))
        else :
            print(bannar_open_lock)

        while True :

            if self.colored :
                main_prompt = input(colored(f'\n{self.prompter}', self.colored)).lower().strip()
            else :
                main_prompt = input(f'\n{self.prompter}').lower().strip()
            
            if self.general_commands(main_prompt) is False :
                if self.user_commands(main_prompt) is False :
                    print('Command Not Found')

    
    def create_secret(self):
            website = input('Website : ').lower().strip()

            login = input('Login Parameter : ').lower().strip()

            password = ''

            i = 0
            while i < 3 :
                password = password_gen()
                print(f'\n(Generated-Secret) {password}')
                agree = input('Save? [Y/n] ').strip().lower()

                if agree in ['y', ''] :
                    break
                else :
                    i += 1
                    continue

            if i == 3 :
                print('\n(Alert) Profile Not Saved')
                return False

            password_encrypted =\
            secret_crypto_action(self.key, password, action='encrypt')

            start = password_status('start')
            expiry = password_status('setexpiry')

            saved = DBHandler.save_secret(profilename=self.user,\
                    website= website ,\
                    db_buffer_to_save= {\
                    'login': login,\
                    'password': str(password_encrypted)[2:-1],\
                    'start': start, 'expiry': expiry 
                                        } )

            if saved == True :

                print(f'\n(Successful) Secret for [{website}] Added')
                print(f'(Successful) Secret is {password}')
                print(f'\n(Successful) Screen will be cleared in 10 seconds')

                sleep(10)
                os.system('cls' if os.name == 'nt' else 'clear')

                if self.colored:
                    print(colored(bannar_secret, self.colored))
                else :
                    print(bannar_secret)
                return
            else : 
                print(saved)

    def help_msg(self) :
        print("\n- (sec) create-secret\n- (h) help\n- (i) info\n- (c) clear\n\
- (e) exit\n- (re) restart")

    def user_commands(self, command) :

        if command in ['test'] :
            print('test')
     
        elif command in ['create-secret', 'sec'] :
            self.create_secret()

        elif command in ['get-password', 'g'] :

            # TESTING BLOCK
            ################
            login = input('\nWhich Login? ')
            print('-'*22)
            p = DBHandler.get_password(self.user, 'secretdb.json', website=login)

            d = secret_crypto_action(self.key, p, 'decrypt')
            print(p)
            print('-'*22)
            print(d)
            ################

        elif command in ['quit', 'q'] :
            print(f'\n(Quitting Profile)')
            raise KeyboardInterrupt

        else :
            return False
        
