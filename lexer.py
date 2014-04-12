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
t_EQUALS   = r'='
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

# ((true|false|'.*'|[a-zA-Z_][a-zA-Z_0-9\_]*|[a-zA-Z_][a-zA-Z_0-9\_]*.[a-z]),)
# DAMN THIS
# \[( ( (true|false)* | ('.*')* | ([a-zA-Z_][a-zA-Z_0-9\_]*|[a-zA-Z_][a-zA-Z_0-9\_]*.[a-z])*)* ,)*\]
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

#def t_WHITESPACE(t):
#    r'\s'
#    pass

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()

file1 = open("program2.txt", "r")
data = file1.read()
file1.close()

lexer.input(data)

for tok in lexer:
    print tok
