import ply.yacc as yacc
from jit_lexer import *
from jit_ast import *
from jit_symboltable import * #PJ

class Parser():
    
    ST = SymbolTable() #PJ

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
        #PJ 
        if len(p) == 5: # first production
            p[0] = AstBinOp(AstID(p[2], p[1]),p[3],p[4])
            var_name = p[2] # lexeme for identifier
            var_type = p[1] # AST node return for type
            var_value = p[4].value # value of the expr as given by the AST
            var_record = {'name': var_name, 'type': var_type, 'value': var_value}
            j = Parser.ST.searchRecord(var_name)
            if j == -1:
                Parser.ST.addRecord(var_record)
            else:
                Parser.ST.updateRecord(j,var_record)
            #print p[2]
            #print var_record
            #print self.ST
        elif len(p) == 4:
            p[0] = AstBinOp(AstID(p[1]),p[2],p[3])
            var_name = p[1]
            #var_type = p[1]
            var_value = p[3].value
            #var_record = {'name': var_name, 'type': var_type, 'value': var_value}
            # check for overriding 
            j = Parser.ST.searchRecord(var_name)
            # print "testing new ST creation"
            # new_ST = SymbolTable()
            # Parser.ST.copyRecords(new_ST)
            if j == -1: # record not found
                #self.ST.addRecord(var_record)
                print "Semantic error: Initialization without declaration"
            else:
                #self.ST.updateRecord(j,var_record)
                #print var_value
                Parser.ST.table[j]['value'] = var_value
            #print self.ST
        elif len(p) == 3:
            p[0] = AstVarDecl(p[2], p[1])
            var_name = p[2]
            var_type = p[1]
            var_value = 0 # default value
            var_record = {'name': var_name, 'type': var_type, 'value': var_value}
            j = Parser.ST.searchRecord(var_name)
            if j == -1:
                Parser.ST.addRecord(var_record)
            else:
                Parser.ST.updateRecord(j,var_record)
            #print var_record
            #print self.ST

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
                    | ID EQUALS expression'''

        if p[1].startswith('"'):
            p[0] = [AstString(p[1])]
        elif len(p) == 4:
            p[0] = [AstBinOp(AstID(p[1]), p[2], p[3])]
        else:
            p[0] = [AstID(p[1])]
            


    def p_type(self, p):
        '''type : STRING
                | BOOLEAN
                | INT
                | NODE
                | LIST
                | GRAPH'''
        #p[0] = AstEmpty() right if you want nothing to be returned for type

        p[0] = p[1] #Needed for ST!! #PJ string, boolean

    def p_expression(self, p):
        '''expression : arithmetic_expr
                      | STRING_s
                      | BOOLEAN_s
                      | LIST_s
                      | function_call
                      '''
        if (type(p[1]) is str) and (p[1].startswith('"')):
            p[0] = AstString(p[1])
        else:
            p[0] = p[1]

    #def p_expression_call(self, p):
    #   '''expression : function_call'''
    #  p[0] = AstFun(p[1])

    def p_arithmetic_expr(self, p):
        '''arithmetic_expr : arithmetic_expr '+' term
                           | arithmetic_expr '-' term
                           | term'''
        p[0] = p[1]

    def p_empty(self, p):
        'empty :'
        p[0] = AstEmpty()

    def p_term(self, p):
        '''term : term '*' factor
                | term '/' factor
                | factor'''
        p[0] = p[1]

    def p_factor(self, p):
        '''factor : LPAREN arithmetic_expr RPAREN
                  | ID
                  | NUM'''
        p[0] = AstNum(p[1])

    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)

    def __init__(self):
        lexer = Lexer()
        self.tokens = tokens = lexer.tokens
        
        self.parser = yacc.yacc(module=self)
