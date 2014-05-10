import ply.yacc as yacc
from jit_lexer import *
from jit_ast import *
from jit_symboltable import *

import re

class Parser():

    ST = SymbolTable()
    
    def p_statement(self, p):
        '''statement : variable_decl
                     | function_call
                     | function_decl
                     | for_loop
                     | if_block
                     | empty
                     '''
        p[0] = p[1]

    def p_variable_decl(self, p):
        '''variable_decl : type ID EQUALS expression
                         | ID EQUALS expression
                         | type ID'''

        if len(p) == 5:
            # type ID EQUALS expression
            p[0] = AstBinOp(AstID(p[2], p[1]), p[3], p[4])
            # Semantic Checking: building a new record
            var_type = p[1]
            var_name = p[2]
            var_record = {'name': var_name, 'type': var_type }
            j = Parser.ST.searchRecord(var_name)
            if j == -1:
                Parser.ST.addRecord(var_record)
            else:
                Parser.ST.updateRecord(j,var_record) # this completely overwrites the previous var
        elif len(p) == 4:
            # ID EQUALS expression
            if isinstance(p[3], str):
                p[3] = AstString(p[3])
            p[0] = AstBinOp(AstID(p[1]), p[2], p[3])
            # Semantic Checking: 
            var_name = p[1]
            var_type = p[3].type # NEED TYPE FROM AST CLASS
            print " $$$$$$$ var name :: " + str(var_name) + " $$$$$$$$$"
            print " $$$$$$$ var type :: " + str(var_type) + " $$$$$$$$$"
            var_record = {'name': var_name, 'type': var_type }
            j = Parser.ST.searchRecord(var_name)
            if j == -1:
                print "Semantic error: Initialization without declaration"
            else:
                if (Parser.ST.getRecordType(j) is var_type):
                    self.ST.updateRecord(j,var_record)
                else:
                    print "Semantic error: Type mismatch in redeclared variable " + var_name
        elif len(p) == 3:
            # type ID
            p[0] = AstVarDecl(p[2], p[1])
            # Semantic Checking:
            var_type = p[1]
            var_name = p[2]
            var_value = 0 # default value
            var_record = {'name': var_name, 'type': var_type, 'value': var_value}
            j = Parser.ST.searchRecord(var_name)
            if j == -1:
                Parser.ST.addRecord(var_record)
            else:
                Parser.ST.updateRecord(j,var_record)

    def p_function_call(self, p):
        '''function_call : fun LPAREN parameters RPAREN'''
        p[1].params = p[3]
        p[0] = p[1]

    def p_func_decl(self, p):
        '''function_decl : NEWFUN ID LPAREN variable_list RPAREN LBRACE statement_list RBRACE'''
        p[0] = AstFunDecl(p[2], p[4], p[7])

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

    def p_variable_list(self, p):
        '''variable_list : empty
            | variable_decl COMMA variable_list
            | variable_decl'''
        if not p[1]:
            # No var passed
            p[0] = []
        elif len(p) == 2:
            # one variable_decl
            p[0] = [p[1]]
        elif len(p) == 4:
            # variable_decl COMMA variable_list
            p[0] = [p[1]] + p[3]

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
        '''expression : operations
                      | article_arithmetic
                      | STRING_s
                      | LIST_s
                      | function_call
                      '''

        # STRING_s
        if (type(p[1]) is str):
            if (p[1].startswith('"')):
                p[0] = AstString(p[1])
            elif (p[1].startswith('[')):
                p[0] = AstList(p[1])

        # TODO: Do we need more here?
        else :
            p[0] = p[1]
            
    def p_article_arithmetic(self, p):
        '''article_arithmetic : ID UNION ID optional_part
                              | ID INTERSECTION ID optional_part
                              '''
        p[0] = AstEmpty()
    
    def p_optional_part(self, p):
        '''optional_part : OVER things_list
                         | empty
                         '''
        p[0] = AstEmpty()
        
    def p_things_list(self, p):
        '''things_list : thing
                       | thing COMMA things_list
                       '''
        p[0] = AstEmpty()
    
    def p_thing(self, p):
        '''thing : KEYWORDS
                 | BODY
                 | PUBLISHER
                 | TITLE
                 | AUTHOR
                 | DATE
                 '''
        p[0] = AstEmpty()
    
    def p_operations(self, p):
        '''operations : s
                      '''
        #if len(p) == 3:
        #    p[0] = AstBinOp(AstEmpty(), p[1], p[2])
        #else:
        p[0] = p[1]
            
    def p_s(self, p):
        '''s : s OR t
             | t
             '''
        if len(p) == 4:
            p[0] = AstBinOp(p[1], p[2], p[3])
        else:
            p[0] = p[1]
    
    def p_t(self, p):
        '''t : t AND f
             | f
             '''
        if len(p) == 4:
            p[0] = AstBinOp(p[1], p[2], p[3])
        else:
            p[0] = p[1]

    def p_f(self, p):
        '''f : f EQUALS_c g
             | f NOT_EQUALS_c g
             | g
             '''
        if len(p) == 4:
            p[0] = AstBinOp(p[1], p[2], p[3])
        else:
            p[0] = p[1]

    def p_g(self, p):
        '''g : g LESS_c j
             | g LESS_EQUALS_c j
             | g GREATER_c j
             | g GREATER_EQUALS_c j
             | NOT g
             | j
             '''
        # print "im in less and greater production, 1 and 3 " + str(p[1]) + " " + str(p[3])
        if len(p) == 4:
            p[0] = AstBinOp(p[1], p[2], p[3])
        elif len(p) == 3:
            p[0] = AstBinOp(AstEmpty(), p[1], p[2])
        else:
            p[0] = p[1]

    def p_j(self, p):
        '''j : j '+' k
             | j '-' k
             | k
             '''
        # print "im in + and - production, 1 and 3 " + str(p[1]) + " " + str(p[3])
        if len(p) == 4:
            p[0] = AstBinOp(p[1], p[2], p[3])
        else:
            p[0] = p[1]

    def p_k(self, p):
        '''k : k '*' l
             | k '/' l
             | l
             '''
        if len(p) == 4:
            print "im in * and / production, 1 and 3 " + str(p[1]) + " " + str(p[3])
            p[0] = AstBinOp(p[1], p[2], p[3])
            # pass in another arg to binop for the type of each node
        else:
            p[0] = p[1]

    def p_l(self, p):
        '''l : LPAREN operations RPAREN 
             | ID
             | NUM
             | BOOLEAN_s
        '''
        if len(p) == 4:
            p[0] = p[2]
        elif type(p[1]) is str:
            if p[1] in ['true', 'false']:
                p[0] = AstString(p[1])
            else:
                # get type from ST and make 2nd arg to AstID
                id_type = Parser.ST.getRecordType(Parser.ST.searchRecord(p[1]))
                p[0] = AstID(p[1], id_type)
        else:
            p[0] = AstNum(p[1], 'int')

    def p_empty(self, p):
        'empty :'
        p[0] = AstEmpty()

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
        p[0] = AstIfBlock(p[3], p[7], p[11])
        
    def p_error(self, p):
        print "Syntax error at '%s'" % p.value
        print "in line '%d'" % p.lineno
        print "at position '%d'" % p.lexpos
        # Just stop compiling right here I guess.

    def __init__(self):
        lexer = Lexer()
        self.tokens = tokens = lexer.tokens

        self.parser = yacc.yacc(module=self)

