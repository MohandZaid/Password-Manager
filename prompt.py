import os , sys

from termcolor import colored

from functions import *
from database import *

banner = '''
    ____                  __  ___                
   / __ \____  ____ _____/  |/  /___  ____  _____
  / /_/ / __ `/ ___` ___/ /|_/ / __ \/ __ \/ ___/
 / ____/ /_/.(__  |__  ) /  / / / / / /_/ / /    
/_/    \__,_/____/____/_/  /_/_/ /_/\__, /_/     
                 By`Mohand Zaid`/_______/        

                '''

dev = 'Developed By: Mohand Zaid (mohandzaid33@gmail.com)'
help_msg = '(h)help to show commands!'
 

class Prompt :

    def __init__(self, prompter=' PssMngr > ', color=False) :
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
            
            if self.prompt_functions(main_prompt) is False :
                print('Command Not Found')
            
    def help_msg(self) :
        print("- (h)help\n- (i)info\n- (c)clear\n- (e)exit\n- (re)restart\n- (mkpf)mkprofile")

    def prompt_functions(self, command):

        if command in ['help', 'h'] :
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

        elif command == '':
            pass

        elif command in ['mkprofile', 'mkpf'] :

            username = input('Username : ').lower().strip()
            email = input('Email : ').lower()
            master_password = input('Password : ').strip()
            confirm_pass = input('Confirm-Password : ').strip()

            pf_data = make_profile(username, email, master_password, confirm_pass)

            if pf_data == 'false_username' :
                print('Invalid Username')

            if pf_data == 'false_email' :
                print('Invalid Email')

            elif pf_data :
                print('Profile Added')
                DBHandler(pf_data['username'], pf_data['email'], pf_data['master_password'])


        else:
            return False
        
    def restart(self):
        
        print("\nRestarting PassMngr ...\n")
        app = sys.executable
        os.execl(app, app, *sys.argv)


class UserPrompt(Prompt) :

    def __init__(self, user, prompter=' user > ', color=False):

        self.user = user
        self.prompter = prompter
        self.colored = color

        self.prompter = f' {self.user}@PassMngr > '

        while True :

            if self.colored :
                main_prompt = input(colored(f'{self.prompter}', 'yellow')).lower().strip()
            else :
                main_prompt = input(f'{self.prompter}').lower().strip()
            
            if self.prompt_functions(main_prompt) is None :
                continue
            elif self.user_functions(main_prompt) is False :
                print('Command Not Found2')

    def help_msg(self) :
        print("- (h)help\n- (t)test")

    def user_functions(self, command) :

        if command in ['test'] :
            print('test')

        else :
            return False
        

# Debugging
# u = UserPrompt('mohand', color=True)
u = Prompt(color=True)