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
        'in': 'IN',
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'newfun': 'NEWFUN',
        'over': 'OVER',
        'KEYWORDS': 'KEYWORDS',
        'AUTHOR': 'AUTHOR',
        'PUBLISHER': 'PUBLISHER',
        'DATE': 'DATE',
        'BODY': 'BODY',
        'TITLE': 'TITLE'
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
        'EQUALS_c',
        'LESS_c',
        'LESS_EQUALS_c',
        'GREATER_c',
        'GREATER_EQUALS_c',
        'NOT_EQUALS_c',
        'COMMA',
        'UNION',
        'INTERSECTION'
        ] + list(reserved.values())

    # Literals
    literals = ['+','-','*','/']

    # Regular expression rules for simple tokens
    # == 
    t_UNION = r'\+\+'
    t_INTERSECTION = r'\^\^'
    t_NOT_EQUALS_c = r'!='
    t_LESS_c = r'<'
    t_LESS_EQUALS_c = r'<='
    t_GREATER_c = r'>'
    t_GREATER_EQUALS_c = r'>='
    t_EQUALS_c = r'=='
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
        r'\[(([ \t]*)([0-9]|true|false|"[^"]*"|[a-zA-Z_][a-zA-Z_0-9\_]*|[a-zA-Z_][a-zA-Z_0-9\_]*.[a-z]+)([ \t]*),([ \t]*))*\]'
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
        print "in line '%d'" % t.lexer.lineno
        print "at position '%d'" % t.lexer.lexpos
        t.lexer.skip(1) # Should we really skip? No I guess. Just stop compiling right here.
    
    def __init__(self):
        lex.lex(module=self)

########## Grammar needed for prog1 and prog2 ##########
''' 
    statement : variable_decl
             | function_call
             | function_decl
             | for_loop
             | if_block
             | empty

    variable_decl : type ID EQUALS expression
             | ID EQUALS expression
             | type ID

    function_call : fun LPAREN parameters RPAREN

    function_decl : NEWFUN ID LPAREN variable_list RPAREN LBRACE statement_list RBRACE

    variable_list : empty
            | variable_decl COMMA variable_list
            | variable_decl

    for_loop : FOR ID IN ID LBRACE statement_list RBRACE

    statement_list : statement
            | statement_list statement
    
    if_block : IF ( expression ) THEN { statement_list } ELSE { statement_list }'

    fun : SAY
            | LISTEN
            | IMPORT
            | SAVE
            | GET
            | PUSH
            | PULL
            | CREATENODE
            | SEARCH

    parameters : empty
            | parameter COMMA parameters
            | parameter
    
    parameter : ID
            | STRING_s
            | LIST_s
            | BOOLEAN_s
            | ID EQUALS expression

    type : STRING
            | BOOLEAN
            | INT
            | NODE
            | LIST
            | GRAPH

    expression : operations
            | STRING_s
            | LIST_s
            | function_call

    operations : NOT operations
            | s

    s : s OR t
            | t

    t : t AND f
            | f

    f : f EQUALS_c g
            | f NOT_EQUALS_c g
            | g
    
    g : g LESS_c j
            | g LESS_EQUALS_c j
            | g GREATER_c j
            | g GREATER_EQUALS_c j
            | j

    j : j '+' k
            | j '-' k
            | k

    k : k '*' l
            | k '/' l
            | l
    
    l : LPAREN operations RPAREN 
            | ID
            | NUM
            | BOOLEAN_s

    empty :

        '''
