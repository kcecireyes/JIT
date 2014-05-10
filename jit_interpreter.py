from jit_parser import *
from pprint import pprint
from jit_ast_visitor import *

class Interpreter:
    def __init__(self, output_filename="temp.py"):
        self.visitor = AstVisitor()
        self.output = open(output_filename, 'w')

    def execute_ast(self, ast_node, debug=False):
        code = ast_node.accept(self.visitor)
        if debug:
            print "code = " + code
        self.output.write(code)
        exec code in globals()

        # if hasattr(ast_node, 'right'):
        #     ast_node.right = self.execute_ast(ast_node.right)
        #
        # if hasattr(ast_node, 'left'):
        #     ast_node.left = self.execute_ast(ast_node.left)
        #
        # if (ast_node.type == "fun"):
        #     if ast_node.subtype == "say":
        #         print ast_node.child.value
        #     elif ast_node.subtype == "listen":
        #         raw_input("User input: ")

    def execute_txt(self, code, debug=True):
        parser = Parser()
        ast = parser.parser.parse(code)
        if debug:
            print "AST:"
            for line in str(ast).split('\n'):
                print "\t"+line

        self.execute_ast(ast, debug=debug)

        if debug:
            print "\n"
