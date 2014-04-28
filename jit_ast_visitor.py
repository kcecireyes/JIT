from jit_code_generator import *

class AstVisitor:
    def __init__(self, filename):
        self.output = open(filename, 'w')
        self.code_generator = CodeGenerator()
        #list of dicts
        self.env = []

    def enter_scope(self, env):
        self.env.append(env)

    def exit_scope(self):
        self.env.pop()
        
        
        
    def visit_fun(self, fun_node):
        if fun_node.subtype == "say":
            sentences = (param.accept(self) for param in fun_node.params)
            lst = self.code_generator.generate_list(sentences)
            prtstr = "'\\n'.join(%s)" % lst
            code = self.code_generator.generate_print(prtstr)
            self.output.write(code + '\n')

        if fun_node.subtype == "createnode":
            print "Node()"
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
        if binop_node.op == "EQUALS":
            lhs = binop_node.left.accept(self)
            rhs = binop_node.right.accept(self)
            self.env[-1][lhs] = rhs
        

    def visit_str(self, str_node):
        pass


    def visit_num(self, str_node):
        pass

