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
    option_parser.add_option("--debug", action="store_true", dest="debug", default=False)
    (options, args) = option_parser.parse_args()

    if (options.filename):
        # Note: Input file must end with a new line character
        interpreter = Interpreter(re.sub('.txt', '.gen.py', options.filename))

        with open(options.filename, "r") as file:
            data = file.readlines()

        overflow = ""
        for i, line in enumerate(data):
            line = overflow + line

            if line.count('{') == line.count('}'):
                if options.debug:
                    print "=======%s" %line

                interpreter.execute_txt(line.strip(), line=i, debug=options.debug)
                overflow = ""
            else:
                overflow = line

    else:
        interpreter = Interpreter()
        while True:
            try:
                line = raw_input("JIT> ")
            except KeyboardInterrupt:
                # Execute, don't crash
                print '''
      _____  ____    ____    ___    ___  __  __  ____  __
     / ___/ / __ \  / __ \  / _ \  / _ ) \ \/ / / __/ / /
    / (_ / / /_/ / / /_/ / / // / / _  |  \  / / _/  /_/
    \___/  \____/  \____/ /____/ /____/   /_/ /___/ (_)
                '''
                exit()

            while line.count('{') != line.count('}'):
                line = line + raw_input("... ")

            try:
                interpreter.execute_txt(line, debug=options.debug)
            except NameError:
                # Already prints error
                pass
            except AttributeError:
                print "There was a problem parsing that line (AttributeError)."


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
