from jit_code_generator import *

class AstVisitor:
    def __init__(self, filename):
        self.output = open(filename, 'w')
        self.code_generator = CodeGenerator()
        
    def visit_fun(self, fun_node):
        if fun_node.subtype == "say":
            sentences = (str(st) for st in fun_node.params)
            lst = self.code_generator.generate_list(sentences)
            prtstr = "'\\n'.join(%s)" % lst
            code = self.code_generator.generate_print(prtstr)
            self.output.write(code + '\n')
        if fun_node.subtype == "createnode":
            self.output.write("Node()")

    def visit_binop(self, binop_node):
        prtstr = str(binop_node.left) + " " + str(binop_node.op) + " " + str(binop_node.right) + "\n"
        self.output.write(prtstr)

    def visit_str(self, str_node):
        pass
