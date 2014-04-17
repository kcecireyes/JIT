from jit_parser import *
from pprint import pprint

class Interpreter:

    def execute_ast(self, ast_node):
        # # Something like this?
        
        if hasattr(ast_node, 'right'):
            ast_node.right = self.execute_ast(ast_node.right)
            
        if hasattr(ast_node, 'left'):
            ast_node.left = self.execute_ast(ast_node.left)
        
        if (ast_node.type == "fun"):
            if ast_node.subtype == "say":
                print ast_node.child.value
            elif ast_node.subtype == "listen":
                raw_input("User input: ")
            
    def execute_txt(self, code):
        parser = Parser()
        ast = parser.parser.parse(code)
        print "AST:"
        for line in ast.to_string().split('\n'):
            print "\t"+line
        self.execute_ast(ast)
        print "\n"