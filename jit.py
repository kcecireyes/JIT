#!/usr/bin/python
from optparse import OptionParser
import glob
import ply.yacc as yacc
import ply.lex as lex

# Good references:
# https://github.com/xerox91/Simple-Compiler/blob/master/compiler.py
# https://github.com/dabeaz/ply/blob/master/example/GardenSnake/GardenSnake.py


class Lexing():
	keywords = {}
	tokens = {}
	# lex.lex() ?

class Parsing():
	tokens = Lexing.tokens
	# yacc.parse(s) ?

class Compiler():
	def __init__(self):
		self.lex = Lexing()
		self.parse = Parsing()
		
#	def init(self):
#		self.lex.build()

	def compile(self, path, verbose=False):
		# Print file to screen
		self.jit_code = open(path, 'r')
		print path+":"
		for line in self.jit_code:
			print "\t"+line
		print "\n"

def main():
	parser = OptionParser()
	jit_compiler = Compiler()
#	jit_compiler.init()
	
	
	parser.add_option("-f", "--file", dest="filename", help="JIT program filename", type="string")
	(options, args) = parser.parse_args() 

	if (options.filename):
		jit_compiler.compile(options.filename, True)
	else:
		# Compile everything in this folder
		for fname in glob.glob('*.jit'):
			jit_compiler.compile(fname, True)

if __name__ == '__main__':
    main()
