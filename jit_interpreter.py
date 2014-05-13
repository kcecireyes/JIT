from jit_parser import *
from pprint import pprint
from jit_ast_visitor import *
import os.path

class Interpreter:
    def __init__(self, output_filename=None):
        self.visitor = AstVisitor()

        if output_filename == None:
            self.output = None
            # exec "import jitlib" in globals()
        else:
            self.output = open(output_filename, 'w')
            self.output.write("#!/usr/bin/python\n")
            self.output.write("import os.path, sys\n")
            self.output.write('sys.path.append("'+os.path.dirname(os.path.realpath(__file__))+'")\n')
            self.output.write("from jitlib.node import Node, Keyword, node_get\n")
            self.output.write("from jitlib.jit_nlp import *\n")
            self.output.write("from jitlib.graf import search, pull\n")
            self.output.write("from jitlib.database import engine, Base\n")
            self.output.write("Base.metadata.create_all(engine)\n")
            self.output.write("\n")
            self.output.write("\n")

    def execute_ast(self, ast_node, debug=False):
        code = ast_node.accept(self.visitor)
        if debug:
            print "code = {" + code[:-1] + "}"

        if self.output == None:
            return code
        else:
            self.output.write(code)

    def execute_txt(self, code, line=0, debug=False):
        parser = Parser()
        ast = parser.parser.parse(code)
        if debug:
            print "AST:"
            for line in str(ast).split('\n'):
                print "\t"+line

        code = self.execute_ast(ast, debug=debug)

        if debug:
            print "\n"

        return code
