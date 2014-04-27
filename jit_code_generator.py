class CodeGenerator:
    def __init__(self):
        pass

    def generate_list(self, elements):
        return '[%s]' % ', '.join(elements)

    def generate_asssignment(self, lfh, rhs):
        return '%s = %s' % (lfh, rhs)

    def generate_print(self, string):
        return 'print %s\n' % string

    def generate_assignment(self, lhs, rhs):
        return '%s = %s\n' %(lhs, rhs)
