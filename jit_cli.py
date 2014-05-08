#!/usr/bin/python
from optparse import OptionParser
from jit_interpreter import *
import re

try:
    import readline
except ImportError:
    # no readline on Windows
    pass

def main():
    # This code allows us to run any program file using the CLI.
    option_parser = OptionParser()
    option_parser.add_option("-f", "--file", dest="filename", help="JIT program filename", type="string")
    option_parser.add_option("--silent", action="store_false", dest="debug", default=True)
    (options, args) = option_parser.parse_args()

    if (options.filename):
        # Note: Input file must end with a new line character
        interpreter = Interpreter(re.sub('.txt', '.gen.py', options.filename))

        with open(options.filename, "r") as file:
            data = file.readlines()

        overflow = ""
        for line in data:
            line = overflow + line

            if line.count('{') == line.count('}'):
                if options.debug:
                    print "=======%s" %line

                interpreter.execute_txt(line.strip(), options.debug)
                overflow = ""
            else:
                overflow = line

    else:
        interpreter = Interpreter()
        while True:
            line = raw_input("JIT> ")

            while line.count('{') != line.count('}'):
                line = line + raw_input("... ")

            interpreter.execute_txt(line)

    if options.debug:
        print '''
               ____  __  __  _____  ____  ____  ____   __ *
              / __/ / / / / / ___/ / __/ / __/ / __/  / /
             _\ \  / /_/ / / /__  / _/  _\ \  _\ \   /_/
            /___/  \____/  \___/ /___/ /___/ /___/  (_)

            * Maybe. We didn't crash. That's good, right?
        '''

if __name__ == "__main__":
    main()
