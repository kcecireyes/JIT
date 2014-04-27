from jit_code_generator import *

class AstVisitor:
    def __init__(self, filename):
        self.output = open(filename, 'w')
        self.code_generator = CodeGenerator()
        self.env = {}
        
        
    def visit_fun(self, fun_node):
        if fun_node.subtype == "say":
            sentences = (param.accept(self) for param in fun_node.params)
            lst = self.code_generator.generate_list(sentences)
            prtstr = "'\\n'.join(%s)" % lst
            code = self.code_generator.generate_print(prtstr)
            self.output.write(code + '\n')
            

    def visit_binop(self, binop_node):
        pass

    def visit_str(self, str_node):
        pass

        
