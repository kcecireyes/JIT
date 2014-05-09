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
        new_body = []
        for line in body:
            new_body.append('\n\t'.join(line.strip().split('\n')))
                        
        code = 'for %s in %s:\n\t%s' % (itr, span, '\n\t'.join(new_body))
        print code
        return code
        
        

