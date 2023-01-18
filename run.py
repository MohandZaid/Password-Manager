#!/bin/python3
import sys
import importlib

from prompt import Prompt

if __name__ == '__main__':

    try:
        if not importlib.util.find_spec('cryptography') :
            print('(Error) You Need To Install Cryptography Module')
            print('(Error) Run `pip install -r requirements.txt`')
            sys.exit()

        if importlib.util.find_spec('termcolor') :
            Prompt(color='yellow')
        
        else :
            Prompt()

    except KeyboardInterrupt :
        sys.exit()
    except EOFError :
        sys.exit()

    finally:
        print('\nExiting PassMngr.\n')
