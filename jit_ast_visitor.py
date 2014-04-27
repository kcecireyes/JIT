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
        else:
            self.output.write("ERROR visit_fun\n")

    def visit_binop(self, binop_node):
        if(binop_node.right.type == "string"):
            prtstr = str(binop_node.left) + " " + str(binop_node.op) + " " + str(binop_node.right) + "\n"
        elif(binop_node.right.type == "function"):
            prtstr = str(binop_node.left) + " " + str(binop_node.op) + " " + "\n"
            self.visit_fun(binop_node.right)
        else:
            prtstr = "ERROR visit_binop\n"

        self.output.write(prtstr)

    def visit_str(self, str_node):
        pass

    def visit_num(self, str_node):
        pass
