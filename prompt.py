import os , sys

from termcolor import colored


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

    def __init__(self, prompter=' Main > ', color=False) :
        self.prompter = prompter
        self.colored = color

        if self.colored :
            print(colored(banner,'yellow'))
        else:
            print(banner)
            print("Colored Mode Off\nrun 'pip install pyfiglet termcolor'and restart program\n")

        while True :

            if self.colored :
                main_prompt = input(colored(f'{self.prompter}', 'yellow')).lower().strip()
            else :
                main_prompt = input(f'{self.prompter}').lower().strip()
            
            self.prompt_functions(main_prompt)


    def prompt_functions(self, user_prompt):

        if user_prompt in ['help', 'h'] :
            print("- (h)help")
        
        elif user_prompt in ['info', 'i'] :
            print(banner)
            print(dev)
            print(help_msg)
    

        elif user_prompt in ['clear', 'c'] :
            os.system('clear')
        
        elif user_prompt in ['restart', 're'] :
            self.restart()

        elif user_prompt in ['e', 'exit'] :
            sys.exit()

        elif user_prompt == '':
            pass
        else :
            print('Command Not Found')


    def restart(self):
        
        print("\nRestarting PassMngr ...\n")
        app = sys.executable
        os.execl(app, app, *sys.argv)
