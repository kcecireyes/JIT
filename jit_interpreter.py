from jit_parser import *
from pprint import pprint
from jit_ast_visitor import *

class Interpreter:
    def __init__(self, output_filename="temp.py"):
        self.visitor = AstVisitor(output_filename)

    def execute_ast(self, ast_node):
        ast_node.accept(self.visitor)
        
    def execute_txt(self, code):
        parser = Parser()
        ast = parser.parser.parse(code)
        print "AST:"
        for line in str(ast).split('\n'):
            print "\t"+line
        self.execute_ast(ast)
        print "\n"
