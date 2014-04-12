from compiler import ast
from lexer import Lexer
from ply import yacc

class Parser():
    # Helper function
    def Assign(self, left, right):
        names = []
        if isinstance(left, ast.Name):
            # Single assignment on left
            return ast.Assign([ast.AssName(left.name, 'OP_ASSIGN')], right)
        elif isinstance(left, ast.Tuple):
            # List of things - make sure they are Name nodes
            names = []
            for child in left.getChildren():
                if not isinstance(child, ast.Name):
                    raise SyntaxError("that assignment not supported")
                names.append(child.name)
            ass_list = [ast.AssName(name, 'OP_ASSIGN') for name in names]
            return ast.Assign([ast.AssTuple(ass_list)], right)
        else:
            raise SyntaxError("Can't do that yet")


    # The grammar comments come from Python's Grammar/Grammar file

    ## NB: compound_stmt in single_input is followed by extra NEWLINE!
    # file_input: (NEWLINE | stmt)* ENDMARKER
    def p_file_input_end(self, p):
        """file_input_end : file_input ENDMARKER"""
        p[0] = ast.Stmt(p[1])

    def p_file_input(self, p):
        """file_input : file_input NEWLINE
                      | file_input stmt
                      | NEWLINE
                      | stmt"""
        if isinstance(p[len(p)-1], basestring):
            if len(p) == 3:
                p[0] = p[1]
            else:
                p[0] = [] # p == 2 --> only a blank line
        else:
            if len(p) == 3:
                p[0] = p[1] + p[2]
            else:
                p[0] = p[1]
            

    # funcdef: [decorators] 'def' NAME parameters ':' suite
    # ignoring decorators
    def p_funcdef(self, p):
        "funcdef : DEF NAME parameters COLON suite"
        p[0] = ast.Function(None, p[2], tuple(p[3]), (), 0, None, p[5])
    
    # parameters: '(' [varargslist] ')'
    def p_parameters(self, p):
        """parameters : LPAR RPAR
                      | LPAR varargslist RPAR"""
        if len(p) == 3:
            p[0] = []
        else:
            p[0] = p[2]
    

    # varargslist: (fpdef ['=' test] ',')* ('*' NAME [',' '**' NAME] | '**' NAME) | 
    # highly simplified
    def p_varargslist(self, p):
        """varargslist : varargslist COMMA NAME
                       | NAME"""
        if len(p) == 4:
            p[0] = p[1] + p[3]
        else:
            p[0] = [p[1]]

    # stmt: simple_stmt | compound_stmt
    def p_stmt_simple(self, p):
        """stmt : simple_stmt"""
        # simple_stmt is a list
        p[0] = p[1]
    
    def p_stmt_compound(self, p):
        """stmt : compound_stmt"""
        p[0] = [p[1]]

    # simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
    def p_simple_stmt(self, p):
        """simple_stmt : small_stmts NEWLINE
                       | small_stmts SEMICOLON NEWLINE"""
        p[0] = p[1]

    def p_small_stmts(self, p):
        """small_stmts : small_stmts SEMICOLON small_stmt
                       | small_stmt"""
        if len(p) == 4:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = [p[1]]

    # small_stmt: expr_stmt | print_stmt  | del_stmt | pass_stmt | flow_stmt |
    #    import_stmt | global_stmt | exec_stmt | assert_stmt
    def p_small_stmt(self, p):
        """small_stmt : flow_stmt
                      | expr_stmt"""
        p[0] = p[1]

    # expr_stmt: testlist (augassign (yield_expr|testlist) |
    #                      ('=' (yield_expr|testlist))*)
    # augassign: ('+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' |
    #             '<<=' | '>>=' | '**=' | '//=')
    def p_expr_stmt(self, p):
        """expr_stmt : testlist ASSIGN testlist
                     | testlist """
        if len(p) == 2:
            # a list of expressions
            p[0] = ast.Discard(p[1])
        else:
            p[0] = self.Assign(p[1], p[3])

    def p_flow_stmt(self, p):
        "flow_stmt : return_stmt"
        p[0] = p[1]

    # return_stmt: 'return' [testlist]
    def p_return_stmt(self, p):
        "return_stmt : RETURN testlist"
        p[0] = ast.Return(p[2])


    def p_compound_stmt(self, p):
        """compound_stmt : if_stmt
                         | funcdef"""
        p[0] = p[1]

    def p_if_stmt(self, p):
        'if_stmt : IF test COLON suite'
        p[0] = ast.If([(p[2], p[4])], None)

    def p_suite(self, p):
        """suite : simple_stmt
                 | NEWLINE INDENT stmts DEDENT"""
        if len(p) == 2:
            p[0] = ast.Stmt(p[1])
        else:
            p[0] = ast.Stmt(p[3])
    

    def p_stmts(self, p):
        """stmts : stmts stmt
                 | stmt"""
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    ## No using Python's approach because Ply supports precedence

    # comparison: expr (comp_op expr)*
    # arith_expr: term (('+'|'-') term)*
    # term: factor (('*'|'/'|'%'|'//') factor)*
    # factor: ('+'|'-'|'~') factor | power
    # comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not'

    def make_lt_compare((left, right)):
        return ast.Compare(left, [('<', right),])
    def make_gt_compare((left, right)):
        return ast.Compare(left, [('>', right),])
    def make_eq_compare((left, right)):
        return ast.Compare(left, [('==', right),])


    binary_ops = {
        "+": ast.Add,
        "-": ast.Sub,
        "*": ast.Mul,
        "/": ast.Div,
        "<": make_lt_compare,
        ">": make_gt_compare,
        "==": make_eq_compare,
    }
    unary_ops = {
        "+": ast.UnaryAdd,
        "-": ast.UnarySub,
        }
    precedence = (
        ("left", "EQ", "GT", "LT"),
        ("left", "PLUS", "MINUS"),
        ("left", "MULT", "DIV"),
        )

    def p_comparison(self, p):
        """comparison : comparison PLUS comparison
                      | comparison MINUS comparison
                      | comparison MULT comparison
                      | comparison DIV comparison
                      | comparison LT comparison
                      | comparison EQ comparison
                      | comparison GT comparison
                      | PLUS comparison
                      | MINUS comparison
                      | power"""
        if len(p) == 4:
            p[0] = self.binary_ops[p[2]]((p[1], p[3]))
        elif len(p) == 3:
            p[0] = unary_ops[p[1]](p[2])
        else:
            p[0] = p[1]
                  
    # power: atom trailer* ['**' factor]
    # trailers enables function calls.  I only allow one level of calls
    # so this is 'trailer'
    def p_power(self, p):
        """power : atom
                 | atom trailer"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            if p[2][0] == "CALL":
                p[0] = ast.CallFunc(p[1], p[2][1], None, None)
            else:
                raise AssertionError("not implemented")

    def p_atom_name(self, p):
        """atom : NAME"""
        p[0] = ast.Name(p[1])

    def p_atom_number(self, p):
        """atom : NUMBER
                | STRING"""
        p[0] = ast.Const(p[1])

    def p_atom_tuple(self, p):
        """atom : LPAR testlist RPAR"""
        p[0] = p[2]

    # trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME
    def p_trailer(self, p):
        "trailer : LPAR arglist RPAR"
        p[0] = ("CALL", p[2])

    # testlist: test (',' test)* [',']
    # Contains shift/reduce error
    def p_testlist(self, p):
        """testlist : testlist_multi COMMA
                    | testlist_multi """
        if len(p) == 2:
            p[0] = p[1]
        else:
            # May need to promote singleton to tuple
            if isinstance(p[1], list):
                p[0] = p[1]
            else:
                p[0] = [p[1]]
        # Convert into a tuple?
        if isinstance(p[0], list):
            p[0] = ast.Tuple(p[0])

    def p_testlist_multi(self, p):
        """testlist_multi : testlist_multi COMMA test
                          | test"""
        if len(p) == 2:
            # singleton
            p[0] = p[1]
        else:
            if isinstance(p[1], list):
                p[0] = p[1] + [p[3]]
            else:
                # singleton -> tuple
                p[0] = [p[1], p[3]]


    # test: or_test ['if' or_test 'else' test] | lambdef
    #  as I don't support 'and', 'or', and 'not' this works down to 'comparison'
    def p_test(self, p):
        "test : comparison"
        p[0] = p[1]

    # arglist: (argument ',')* (argument [',']| '*' test [',' '**' test] | '**' test)
    # XXX INCOMPLETE: this doesn't allow the trailing comma
    def p_arglist(self, p):
        """arglist : arglist COMMA argument
                   | argument"""
        if len(p) == 4:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = [p[1]]

    # argument: test [gen_for] | test '=' test  # Really [keyword '='] test
    def p_argument(self, p):
        "argument : test"
        p[0] = p[1]
    
    def p_error(self, p):
        #print "Error!", repr(p)
        raise SyntaxError(p)
    
    def __init__(self, lexer = None):
        if lexer is None:
            lexer = Lexer()
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(start="file_input_end", module=self)

    def parse(self, code):
        self.lexer.input(code)
        result = self.parser.parse(lexer = self.lexer)
        return ast.Module(None, result)
