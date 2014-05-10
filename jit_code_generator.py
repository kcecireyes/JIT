class CodeGenerator:
    def __init__(self):
        pass

    def generate_list(self, elements):
        return '[%s]' % ', '.join(elements)

    #def generate_asssignment(self, lfh, rhs):
    #   return '%s = %s' % (lfh, rhs)

    def generate_print(self, string):
        return 'print %s\n' % string

    def generate_binaryOp(self, lhs, op, rhs):
        return '%s %s %s\n' %(lhs, op, rhs)

    def generate_forloop(self, itr, span, body):
        new_body = self.indent_block(body)
                        
        code = 'for %s in %s:\n\t%s\n' % (itr, span, new_body)
        print code
        return code


    def indent_block(self, lines):
        t = []
        for line in lines:
            t.append('\n\t'.join(line.strip().split('\n')))
        if t[0] != "":
            return '\n\t'.join(t)

        return "pass"
        
    def generate_ifblock(self, ifc, thencls, elsecls):
        thcl = self.indent_block(thencls)
        elcl = self.indent_block(elsecls)
        code = 'if %s:\n\t%s\nelse:\n\t%s\n' %(ifc, thcl, elcl)
        return code
