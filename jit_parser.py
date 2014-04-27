import ply.yacc as yacc
from jit_lexer import *
from jit_ast import *

class Parser():

    def p_statement(self, p):
        '''statement : variable_decl
                      | function_call
                      | empty
                      '''
        # p[0] = AstFun( AstSay(), AstString("Testing") )
        p[0] = p[1]

    def p_variable_decl(self, p):
        '''variable_decl : type ID EQUALS expression
                         | ID EQUALS expression
                         | type ID'''
                         
        # Not perfect, but a start.
        # TODO: Finish this
        if len(p) == 5:
            p[0] = AstBinOp(p[2],p[3],p[4])
        elif len(p) == 4:
            p[0] = AstBinOp(p[1],p[2],p[3])
        elif len(p) == 3:
            p[0] = AstBinOp(p[2],'EQUALS',None)

    def p_function_call(self, p):
        '''function_call : fun LPAREN parameters RPAREN'''
        p[1].params = p[3]
        p[0] = p[1]

    def p_fun(self, p):
        '''fun : SAY
                | LISTEN
                | IMPORT
                | SAVE
                | GET
                | PUSH
                | PULL
                | CREATENODE
                | SEARCH'''
        p[0] = AstFun(p[1])

    def p_parameters(self, p):
        '''parameters : empty
                     | parameter COMMA parameters
                     | parameter'''
        if not p[1]:
            p[0] = []
        elif len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = p[1] + p[3]

    def p_parameter(self, p):
        '''parameter : ID
                    | STRING_s
                    | LIST_s
                    | BOOLEAN_s
                    | NUM
                    | ID EQUALS expression'''
        p[0] = [AstString(p[1])]

    def p_type(self, p):
        '''type : STRING
                | BOOLEAN
                | INT
                | NODE
                | LIST
                | GRAPH'''

    def p_expression(self, p):
        '''expression : arithmetic_expr
                      | function_call
                      | STRING_s
                      | BOOLEAN_s
                      | LIST_s
                      '''
        p[0] = AstString(p[1])

    def p_arithmetic_expr(self, p):
        '''arithmetic_expr : arithmetic_expr '+' term
                           | arithmetic_expr '-' term
                           | term'''

    def p_empty(self, p):
        'empty :'
        p[0] = AstEmpty()

    def p_term(self, p):
        '''term : term '*' factor
                | term '/' factor
                | factor'''

    def p_factor(self, p):
        '''factor : LPAREN arithmetic_expr RPAREN
                  | ID
                  | NUM'''

    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)

    def __init__(self):
        lexer = Lexer()
        self.tokens = tokens = lexer.tokens
        
        self.parser = yacc.yacc(module=self)
