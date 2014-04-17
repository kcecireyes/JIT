from jit_parser import *
from pprint import pprint
from jit_ast_visitor import *

class Interpreter:
    def __init__(self):
        self.visitor = AstVisitor()

    def execute_ast(self, ast_node):
        # # Something like this?
        # ast_node.right = execute_ast(ast_node.right)
        # ast_node.left = execute_ast(ast_node.left)
        # if (ast_node.type = "Add"):
            # ast_node.value = ast_node.left.value + ast_node.right.value
            # ast_node.left.value = ast_node.left.value = None
        #print "node is %s" % ast_node.subtype
        print
        print ast_node.accept(self.visitor)
        pass
        
    def execute_txt(self, code):
        parser = Parser()
        ast = parser.parser.parse(code)
        print "AST:"
        for line in str(ast).split('\n'):
            print "\t"+line
        self.execute_ast(ast)
        print "\n"
