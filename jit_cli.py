#!/usr/bin/python
from optparse import OptionParser
from jit_interpreter import *
import re


def main():

    # This code allows us to run any program file using the CLI.
    option_parser = OptionParser()
    option_parser.add_option("-f", "--file", dest="filename", help="JIT program filename", type="string")
    (options, args) = option_parser.parse_args() 

    if (options.filename):
        # Note: Input file must end with a new line character
        interpreter = Interpreter(re.sub('.txt', '.py', options.filename))

        with open(options.filename, "r") as file:
            data = file.readlines()

        for line in data:
            interpreter.execute_txt( line.strip() )
    else:
        interpreter = Interpreter()
        while True:
            interpreter.execute_txt( raw_input("JIT> ") )

    print '''
           ____  __  __  _____  ____  ____  ____   __
          / __/ / / / / / ___/ / __/ / __/ / __/  / /
         _\ \  / /_/ / / /__  / _/  _\ \  _\ \   /_/ 
        /___/  \____/  \___/ /___/ /___/ /___/  (_)  
    '''

if __name__ == "__main__":
    main()
