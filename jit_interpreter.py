from jit_parser import *
from pprint import pprint
from jit_ast_visitor import *
import os.path

class Interpreter:
    def __init__(self, output_filename=None):
        self.visitor = AstVisitor()

        if output_filename == None:
            self.output = None
            exec "import jitlib" in globals()
        else:
            self.output = open(output_filename, 'w')
            self.output.write("#!/usr/bin/python\n")
            self.output.write("# Be sure to add jitlib to your path!\n")
            self.output.write("import jitlib\n")
            self.output.write("\n")

    def execute_ast(self, ast_node, debug=False):
        code = ast_node.accept(self.visitor)
        if debug:
            print "code = " + code

        if self.output == None:
            exec code in globals()
        else:
            self.output.write(code)

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

    def execute_txt(self, code, debug=False):
        parser = Parser()
        ast = parser.parser.parse(code)
        if debug:
            print "AST:"
            for line in str(ast).split('\n'):
                print "\t"+line

        self.execute_ast(ast, debug=debug)

        if debug:
            print "\n"
