#!/usr/bin/python
from parser import Parser
import sys

from compiler import misc, syntax, pycodegen

class Compiler(object):
    def __init__(self):
        self.parser = Parser()
		
    def compile(self, code, filename="<string>"):
        tree = self.parser.parse(code)
        # print tree
        misc.set_filename(filename, tree)
        syntax.check(tree)
        gen = pycodegen.ModuleCodeGenerator(tree)
        code = gen.getCode()
        return code

def main():
	'''Test code'''
	compile = Compiler().compile

	with open("test.snake") as file:
	    code = file.read()

	# Set up the GardenSnake run-time environment
	def print_(*args):
	    print "-->", " ".join(map(str,args))

	globals()["print"] = print_

	compiled_code = compile(code)

	exec compiled_code in globals()
	print "Done"
	
if __name__ == '__main__':
    main()