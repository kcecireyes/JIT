#!/usr/bin/python

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
	'get' : 'GET',
	'pull': 'PULL',
	'createNode': 'CREATENODE'
}

tokens = [
	'ID',
	'STRING_s',
	'NUM',
	'BOOLEAN_s',
	'LIST_s',
	'LPAREN',
	'RPAREN', 
	'EQUALS',
	'COMMA'
	] + list(reserved.values())

# Literals
literals = ['+','-','*','/']

# Regular expression rules for simple tokens
# == 
t_EQUALS = r'='
t_COMMA  = r','
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# t_ignore  = '\s'
t_ignore_COMMENT = r'//.*'
t_ignore_WHITESPACE = r'\s'

# Regular expression rules with action codes
# use shorthand for ELEMENTS which matches: ID | STRING_s | BOOLEAN_s to specify a LIST_s matching
def t_BOOLEAN_s(t):
	r'true|false'
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*\.[a-z]+|[a-zA-Z_][a-zA-Z_0-9]*' # doesn't match trailing '.'
	t.type = reserved.get(t.value,'ID') # Check for reserved words
	return t

def t_LIST_s(t):
	r"\[(((true|false)* |('.*')*|([a-zA-Z_][a-zA-Z_0-9\_]*|[a-zA-Z_][a-zA-Z_0-9\_]*.[a-z])*)*,)*\]"
	return t

def t_STRING_s(t):
	r"'.*'"
	return t

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
	print "Illegal character '%s'" % t.value[0]
	t.lexer.skip(1)

lex.lex()

########## Grammar needed for prog1 and prog2 ##########
''' 
statement : function_call
			variable_declaration
			for_loop

function_call : fun (parameters)

fun : SAY
	LISTEN
	IMPORT
	SAVE
	GET
	PUSH
	PULL
	SEARCH

parameters : epsilon
			parameter, parameters
			parameter

parameter : IDENTIFIER 
			string_statement
			IDENTIFIER = Expression

variable_declaration : type IDENTIFIER = Expression 
					IDENTIFIER = Expression
					type IDENTIFIER

type : STRING
	  BOOLEAN
	  INT
	  NODE
	  LIST
	  GRAPH

S' -> statement
statement -> variable_decl | function_call
variable_decl -> type ID EQUALS expression
				| ID EQUALS expression
				| type ID
function_call -> fun LPAREN parameters RPAREN
fun -> SAY
	| LISTEN
	| IMPORT
	| SAVE
	| GET
	| PUSH
	| PULL
	| SEARCH
parameters -> empty
			| parameter COMMA parameters
			| parameter
parameter -> ID
			| STRING_s
			| ID EQUALS expression
type -> STRING
		| BOOLEAN
		| INT
		| NODE
		| LIST
		| GRAPH
expression -> arithmetic_expr
			| function_call
			| STRING_s
			| BOOLEAN_s
arithmetic_expr -> arithmetic_expr + term
				 | arithmetic_expr - term
				 | term
term -> term * factor
		| term / factor
		| factor
factor -> LPAREN arithmetic_expr RPAREN
		| ID
		| NUM
empty -> <empty>






'''

# Parser for parsing variable declarations and initializations only

def p_statement(p):
	'''statement : variable_decl
				 | function_call'''

def p_variable_decl(p):
	'''variable_decl : type ID EQUALS expression
					 | ID EQUALS expression
					 | type ID'''

def p_function_call(p):
	'''function_call : fun LPAREN parameters RPAREN'''

def p_fun(p):
	'''fun : SAY
			| LISTEN
			| IMPORT
			| SAVE
			| GET
			| PUSH
			| PULL
			| SEARCH'''

def p_parameters(p):
	'''parameters : empty
				 | parameter COMMA parameters
				 | parameter'''

def p_parameter(p):
	'''parameter : ID
			    | STRING_s
			    | ID EQUALS expression'''

def p_type(p):
	'''type : STRING
			| BOOLEAN
			| INT
			| NODE
			| LIST
			| GRAPH'''

def p_expression(p):
	'''expression : arithmetic_expr
				  | function_call
				  | STRING_s
				  | BOOLEAN_s'''

def p_arithmetic_expr(p):
	'''arithmetic_expr : arithmetic_expr '+' term
					   | arithmetic_expr '-' term
					   | term'''

def p_term(p):
	'''term : term '*' factor
			| term '/' factor
			| factor'''

def p_factor(p):
	'''factor : LPAREN arithmetic_expr RPAREN
			  | ID
			  | NUM'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
	print("Syntax error at '%s'" % p.value)

import ply.yacc as yacc
yacc.yacc()

file1 = open("program3.txt", "r") # Note: Input file must end with a new line character
data = file1.read()
file1.close()

# Lex and parse data from input file line by line
i = 0
while 1:
	j = i
	while (data[i]!='\n'):
		i = i+1
	s = data[j:i]
	i = i+1
	if i == len(data):
		break
	yacc.parse(s)

print 'success.'
