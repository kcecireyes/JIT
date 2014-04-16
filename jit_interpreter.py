from jit_parser import *
from pprint import pprint

class Interpreter:
    # def __init__(self):

    def execute_ast(self, ast_node):
        # # Something like this?
        # ast_node.right = execute_ast(ast_node.right)
        # ast_node.left = execute_ast(ast_node.left)
        # if (ast_node.type = "Add"):
            # ast_node.value = ast_node.left.value + ast_node.right.value
            # ast_node.left.value = ast_node.left.value = None
        print ast_node.child.value
        pass
        
    def execute_txt(self, code):
        parser = Parser()
        ast = parser.parser.parse(code)
        print "AST:"
        for line in ast.to_string().split('\n'):
            print "\t"+line
        self.execute_ast(ast)
        print "\n"