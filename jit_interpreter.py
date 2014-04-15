from jit_parser import *

class Interpreter:
    # def __init__(self):

    def execute_ast(self, ast_node):
        # # Something like this?
        # ast_node.right = execute_ast(ast_node.right)
        # ast_node.left = execute_ast(ast_node.left)
        # if (ast_node.type = "Add"):
            # ast_node.value = ast_node.left.value + ast_node.right.value
            # ast_node.left.value = ast_node.left.value = None
        pass
        
    def execute_txt(self, code):
        parser = Parser()
        ast = parser.parser.parse(code)
        self.execute_ast(ast)