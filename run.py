#!/bin/python3
import sys

from prompt import Prompt

if __name__ == '__main__':

    try:
        Prompt(color=True)

    except KeyboardInterrupt :
        sys.exit()
    except EOFError :
        sys.exit()

    finally:
        print('\nExiting PassMngr.\n')
