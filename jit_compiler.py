#!/usr/bin/python
from jit_parser import *

#Note: Input file must end with a new line character
with open("program3.txt", "r") as file:
    data = file.readlines()

parser = Parser()

for line in data:
    parser.parser.parse(line.strip())

print 'End of lexing and parsing: If no errors were displayed give Prashant (and not Cecilia) a chocolate!\n...\n...\n...\nOh ya and it also means your source program is correct.'