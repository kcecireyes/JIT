import ply.lex as lex

class Lexer():
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
        'createNode': 'CREATENODE',
        'for': 'FOR',
        'in': 'IN'
    }

    tokens = [
        'ID',
        'STRING_s',
        'NUM',
        'BOOLEAN_s',
        'LIST_s',
        'LPAREN',
        'RPAREN',
        'LBRACE',
        'RBRACE', 
        'EQUALS',
        'COMMA'
        ] + list(reserved.values())

    # Literals
    literals = ['+','-','*','/']

    # Regular expression rules for simple tokens
    # == 
    t_EQUALS   = r'='
    t_COMMA  = r','
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'

    # t_ignore  = '\s'
    t_ignore_COMMENT = r'//.*'
    t_ignore_WHITESPACE = r'\s'

    # Regular expression rules with action codes
    # use shorthand for ELEMENTS which matches: ID | STRING_s | BOOLEAN_s to specify a LIST_s matching
    def t_BOOLEAN_s(self, t):
        r'true|false'
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*\.[a-z]+|[a-zA-Z_][a-zA-Z_0-9]*' # doesn't match trailing '.'
        t.type = self.reserved.get(t.value,'ID') # Check for reserved words
        return t

    def t_LIST_s(self, t):
        r'\[(([ \t]*)(true|false|"[^"]*"|[a-zA-Z_][a-zA-Z_0-9\_]*|[a-zA-Z_][a-zA-Z_0-9\_]*.[a-z]+)([ \t]*),([ \t]*))*\]'
        return t

    def t_STRING_s(self, t):
        r'"[^"]*"'
        return t

    def t_NUM(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)
    
    def __init__(self):
        lex.lex(module=self)

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