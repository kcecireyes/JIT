# Author: Prashant Jayannavar (pj2271)
# Homework 1: Question 4
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
# MAIN PROGRAM

tokens = (
    'PRINT',
    'STRING',
    )

t_PRINT   = r'print'

def t_STRING(t):
    r'\"[a-z]*\"'
    #if t.value == "true":
    #    t.value = 1
    #else:
    #    t.value = 0
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
    print(p[1])

def p_expression_print(p):
    'expression : PRINT STRING'
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
