class AstNode: pass

class AstEmpty(AstNode):
    def __str__(self):
        return "Empty"

    def accept(self, visitor):
        return ""

class AstBinOp(AstNode):
    def __init__(self,left,op,right, result_type = 'auto'):
        self.type = "binop"
        self.left = left
        self.right = right
        self.op = op
        self.rtype = str(result_type)

    def __str__(self):
        return str(self.left) + str(self.op) + str(self.right)

    def accept(self, visitor):
        return visitor.visit_binop(self)

class AstFun(AstNode):
    def __init__(self,subtype):
        self.type = "function"
        self.subtype = subtype
        self.params = []
        # self.child

    def __str__(self):
        if isinstance (self.params, AstEmpty): 
            return str(self.subtype) + "\n" + "\n"
        else:
            return str(self.subtype) + "\n" + "\n".join(str(p) for p in self.params)

    def accept(self, visitor):
        return visitor.visit_fun(self)

class AstString(AstNode):
    def __init__(self,value):
        self.type = "string"
        self.value = value

    def __str__(self):
        return self.value

    def accept(self, visitor):
        return visitor.visit_str(self)

class AstList(AstNode):
    def __init__(self, value):
        self.type = "list"
        self.value = value

    def __str__(self):
        return self.value

    def accept(self, visitor):
        return visitor.visit_list(self)

class AstID(AstNode):
    def __init__(self, name, id_type = 'auto'): #type = 'auto'):
        self.name = name
        self.type = str(id_type)

    def accept(self, visitor):
        return visitor.visit_id(self)

    def __str__(self):
        return self.name
    
class AstNum(AstNode):
    def __init__(self,value, num_type = 'auto'):
        self.type = num_type
        self.value = value

    def __str__(self):
        return str(self.value)

    def accept(self, visitor):
        return visitor.visit_num(self)


class AstExpr(AstNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        pass

        
class AstVarDecl(AstNode):
    def __init__(self, name, t):
        self.name = name
        self.type = t

    def accept(self, visitor):
        return visitor.visit_vardecl(self)


class AstForLoop(AstNode):
    def __init__(self, itr, span, body):
        self.itr = itr
        self.span = span
        self.body = body

    def accept(self, visitor):
        return visitor.visit_forloop(self)


class AstIfBlock(AstNode):
    def __init__(self, if_clause, then_clause, else_clause):
        self.if_clause = if_clause
        self.then_clause = then_clause
        self.else_clause = else_clause

    def accept(self, visitor):
        return visitor.visit_ifblock(self)


class AstFunDecl(AstNode):
    def __init__(self, name, varlist, stmtlist):
        self.name = name
        self.varlist = varlist
        self.stmtlist = stmtlist

    def accept(self, visitor):
        return visitor.visit_astfundecl(self)
"""        
class AstSay(AstNode):
    def __init__(self):
        self.type = "say"

    def __str__(self):
        return self.type
"""
 
