#!/usr/bin/python
tokens = (
    'SAY',
    'STRING',
    )

t_SAY   = r'say'

def t_STRING(t):
    r'[\"\']{1}[a-zA-Z]*[\"\']{1}'
    #if t.value == "true":
    #    t.value = 1
    #else:
    #    t.value = 0
    t.value = t.value[1:-1]
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build lexer
import ply.lex as lex
lex.lex()

def p_statement_expr(p):
    'statement : expression'
    # print(p[1])

def p_expression_say(p):
    'expression : SAY STRING'
    print(p[2])

def p_error(p):
    print("Syntax error at '%s'" % p.value)

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('jit > ')
    except EOFError:
        break
    yacc.parse(s)
