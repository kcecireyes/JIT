#!/usr/bin/python
from jit_parser import *

#Note: Input file must end with a new line character
with open("programs/program3.txt", "r") as file:
    data = file.readlines()

parser = Parser()

for line in data:
    parser.parser.parse(line.strip())

print '''
       ____  __  __  _____  ____  ____  ____   __
      / __/ / / / / / ___/ / __/ / __/ / __/  / /
     _\ \  / /_/ / / /__  / _/  _\ \  _\ \   /_/ 
    /___/  \____/  \___/ /___/ /___/ /___/  (_)  
                                             

End of lexing and parsing: If no errors were displayed give Prashant (and not Cecilia) a chocolate!

Oh ya and it also means your source program is correct.
'''