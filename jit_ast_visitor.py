from jit_code_generator import *
from collections import defaultdict

class AstVisitor:
    def __init__(self):
        #self.output = open(filename, 'w')
        self.code_generator = CodeGenerator()
        #list of dicts
        self.env = [defaultdict(lambda:None)]

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
            #self.output.write(code + '\n')

        elif fun_node.subtype == "createNode":
            #self.output.write("Node()")
            code = "Node()"
        elif fun_node.subtype == "listen":
            code = "Listen()"
        elif fun_node.subtype == "push":
            code = "Push()"
        else:
            code = "ERROR visit_fun\n"

        return code

    def visit_binop(self, binop_node):
        if not binop_node: return
        """
        if(binop_node.right.type == "string"):
            prtstr = str(binop_node.left) + " " + str(binop_node.op) + " " + str(binop_node.right) + "\n"
        elif(binop_node.right.type == "function"):
            prtstr = str(binop_node.left) + " " + str(binop_node.op) + " " + "\n"
            self.visit_fun(binop_node.right)
        else:
            prtstr = "ERROR visit_binop\n"

        self.output.write(prtstr)
        """
        
        lhs = binop_node.left.accept(self).strip()
        rhs = binop_node.right.accept(self).strip()
        if binop_node.op == "=":
            self.env[-1][lhs] = rhs
        code = self.code_generator.generate_binaryOp(lhs, binop_node.op, rhs)
        return code
        

    def visit_str(self, str_node):
        return str_node.value


    def visit_num(self, str_node):
        return str(str_node)


    def visit_id(self, id_node):
        name = id_node.name
        current_env = self.env[-1]
        val = current_env[name]
        return name

    def visit_vardecl(self, decl_node):
        init_vals = defaultdict(lambda:None)
        init_vals['string'] =  ''
        init_vals['int'] = 0
        self.env[-1][decl_node.name] = None
        code = "%s = %s\n" % (decl_node.name, str(init_vals[decl_node.type]))
        return code
