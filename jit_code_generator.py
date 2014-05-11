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
        if lhs[-9:] == ".keywords":
            return lhs[:-9]+".set_keywords("+rhs+")\n"
        else:
            return '%s %s %s\n' %(lhs, op, rhs)

    def generate_articleOp(self, lhs, op, rhs, assign_to, list_of_things):
        #return '%s %s %s\n' %(lhs, op, rhs)
        if op == "++":
            if len(list_of_things) == 0:
                code = '%s.keywords = list(set(%s.keywords) | set(%s.keywords))\n' % (assign_to,lhs,rhs) 
                return code
            else:
                code = ''
                for i in list_of_things:
                    attribute = i.lower()
                    if attribute == "keywords":
                        code = code + '%s.keywords = list(set(%s.keywords) | set(%s.keywords))\n' % (assign_to,lhs,rhs) 
                    else:
                        code = code + "%s.%s = %s.%s + ', ' + %s.%s\n" % (assign_to,attribute,lhs,attribute,rhs,attribute)
                return code      
        else:
            if len(list_of_things) == 0:
                pass
            else:
                pass
        

    def generate_forloop(self, itr, span, body):
        new_body = self.indent_block(body)
        code = 'for %s in %s:\n\t%s\n\n' % (itr, span, new_body)
        # print code
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
        code = 'if %s:\n\t%s\nelse:\n\t%s\n\n' %(ifc, thcl, elcl)
        return code

    def generate_fundecl(self, name, varlist, stmtlist):
        fun_body = self.indent_block(stmtlist)
        code = "def %s(%s):\n\t%s\n\n" % (name, ", ".join(varlist), fun_body)
        return code
