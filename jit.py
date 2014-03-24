#!/usr/bin/python

# from optparse import OptionParser
# import glob
import ply.yacc as yacc
import ply.lex as lex

reserved = {
	'string': 'STRING',
	'boolean': 'BOOLEAN',
	'node': 'NODE',
	'int':'INT',
	'list':'LIST',
	'graph': 'GRAPH',
	'say': 'SAY',
	'listen': 'LISTEN',
	'import': 'IMPORT',
	'search': 'SEARCH',
	'save': 'SAVE',
	'push': 'PUSH',
	'pull': 'PULL'
}

tokens = (
	'ID',
	'STRING_s',
	'NUM',
	'BOOLEAN_s',
	# 'LIST_s',
	'LPAREN',
	'RPAREN', 
	'EQUALS',
	'COMMA'
)

# Regular expression rules for simple tokens
t_EQUALS   = r'\='
t_COMMA  = r','
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Regular expression rules with action codes
# use shorthand for ELEMENTS which matches: ID | STRING_s | BOOLEAN_s to specify a LIST_s matching
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9\_]*[.?][a-z]*' # matches trailing '.'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

    def t_STRING_s(t):
    	r'.*'
	t.value = t.value[1:-1].decode("string-escape") # as per GardenSnake, eliminates quotes at the beginning and those escaped
	return t

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)    
	return t

def t_BOOLEAN_s(t):
	r'true|false'
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
	print "Illegal character '%s'" % t.value[0]
	t.lexer.skip(1)


# class Parsing():
# 	tokens = Lexing.tokens

# class Compiler():
# 	def __init__(self):
# 		self.lex = Lexing()
# 		self.parse = Parsing()


# 	def compile(self, path, verbose=False):
# 		# Print file to screen
# 		self.jit_code = open(path, 'r')
# 		print path+":"
# 		for line in self.jit_code:
# 			print "\t"+line
# 		print "\n"

# def main():
# 	parser = OptionParser()
# 	jit_compiler = Compiler()
# #	jit_compiler.init()


# 	parser.add_option("-f", "--file", dest="filename", help="JIT program filename", type="string")
# 	(options, args) = parser.parse_args() 

# 	if (options.filename):
# 		jit_compiler.compile(options.filename, True)
# 	else:
# 		# Compile everything in this folder
# 		for fname in glob.glob('*.jit'):
# 			jit_compiler.compile(fname, True)

# if __name__ == '__main__':
#     main()
