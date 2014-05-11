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
        if op == "++":
            pass
        else:
            lines = []
            for thing in list_of_things:
                if thing in ["KEYWORDS", "BODY"]:
                    lines.append("%s.%s = set(%s.%s) & set(%s.%s)" % (assign_to, thing, lhs, thing, rhs, thing))
                elif thing == "title":
                    pass
                elif thing in ["PUBLISHER", "AUTHOR"]:
                    lines.append("%s.%s = %s.%s if %s.%s == %s.%s else ''" % (assign_to, thing, lhs, thing, lhs, thing, rhs, thing))
                else:
                    
                    
                                 
                
        return '%s %s %s\n' %(lhs, op, rhs)

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
