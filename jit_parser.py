import ply.yacc as yacc
from jit_lexer import *
from jit_ast import *
import re

class Parser():

    def p_statement(self, p):
        '''statement : variable_decl
                     | function_call
                     | for_loop
                     | if_block
                     | empty
                     '''
        p[0] = p[1]

    def p_variable_decl(self, p):
        '''variable_decl : type ID EQUALS expression
                         | ID EQUALS expression
                         | type ID'''

        # Not perfect, but a start.
        # TODO: Finish this

        # What does "finish this" mean?
        # Can you add specific TODOs to the incomplete parts?

        if len(p) == 5:
            # type ID EQUALS expression
            p[0] = AstBinOp(AstID(p[2], p[1]), p[3], p[4])
        elif len(p) == 4:
            # ID EQUALS expression
            if isinstance(p[3], str):
                p[3] = AstString(p[3])
            p[0] = AstBinOp(AstID(p[1]), p[2], p[3])
        elif len(p) == 3:
            # type ID
            p[0] = AstVarDecl(p[2], p[1])

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
            # No params
            p[0] = []
        elif len(p) == 2:
            # parameter
            p[0] = p[1]
        elif len(p) == 4:
            # parameter COMMA parameters
            p[0] = p[1] + p[3]


    def p_parameter(self, p):
        '''parameter : ID
                    | STRING_s
                    | LIST_s
                    | BOOLEAN_s
                    | ID EQUALS expression'''

        if p[1].startswith('"'):
            # STRING_s
            p[0] = [AstString(p[1])]
        elif len(p) == 4:
            # ID EQUALS expression
            if (type(p[3]) is str and p[3].startswith('[')):
                p[0] = [AstBinOp(AstID(p[1]), p[2], (AstList(p[3])))]
            else:
                p[0] = [AstBinOp(AstID(p[1]), p[2], p[3])]
        else:
            # Boolean, list and ID?
            # TODO: Do we need more here?
            p[0] = [AstID(p[1])]

    def p_type(self, p):
        '''type : STRING
                | BOOLEAN
                | INT
                | NODE
                | LIST
                | GRAPH'''
        p[0] = p[1]

    def p_expression(self, p):
        '''expression : arithmetic_expr
                      | STRING_s
                      | BOOLEAN_s
                      | LIST_s
                      | function_call
                      '''

        # STRING_s
        if (type(p[1]) is str) and (p[1].startswith('"')):
            p[0] = AstString(p[1])

        # TODO: Do we need more here?
        else:
            p[0] = p[1]

    def p_arithmetic_expr(self, p):
        '''arithmetic_expr : arithmetic_expr '+' term
                           | arithmetic_expr '-' term
                           | term'''

        if len(p) == 4:
            # term operation term
            p[0] = AstBinOp(p[1], p[2], p[3])
        else:
            # term
            p[0] = p[1]

    def p_empty(self, p):
        'empty :'
        p[0] = AstEmpty()

    def p_term(self, p):
        '''term : term '*' factor
                | term '/' factor
                | factor'''
        if len(p) == 4:
            p[0] = AstBinOp(p[1], p[2], p[3])
        else:
            p[0] = p[1]

    def p_factor(self, p):
        '''factor : LPAREN arithmetic_expr RPAREN
                  | ID
                  | NUM'''
        if len(p) == 4:
            p[0] = p[2]
        elif type(p[1]) is str:
            p[0] = AstID(p[1])
        else:
            p[0] = AstNum(p[1])
    
    def p_for_loop(self, p):
        'for_loop : FOR ID IN ID LBRACE statement_list RBRACE'
        p[0] = AstForLoop(AstID(p[2]), AstID(p[4]), p[6])
        
    def p_statement_list(self, p):
        '''statement_list : statement
                          | statement_list statement
                          '''
        #'statement_list : statement'
        if not p[1]:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]
    
    def p_if_block(self, p):
        'if_block : IF LPAREN expression RPAREN THEN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'
        p[0] = AstEmpty() #to be changed
        
    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)

    def __init__(self):
        lexer = Lexer()
        self.tokens = tokens = lexer.tokens

        self.parser = yacc.yacc(module=self)
