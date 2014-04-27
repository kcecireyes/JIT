class AstNode: pass

class AstBinOp(AstNode):
    def __init__(self,left,op,right):
        self.type = "binop"
        self.left = left
        self.right = right
        self.op = op
        
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

    def accept(self, visitor):
        return visitor.visit_fun(self)

    def __str__(self):
        return str(self.subtype) + "\n" + "\n".join(str(p) for p in self.params)

class AstString(AstNode):
    def __init__(self,value):
        self.type = "string"
        self.value = value

    def __str__(self):
        return self.value

    def accept(self, visitor):
        return visitor.visit_str(self)


class AstID(AstNode):
    def __init__(self, identifier, env):
        self.identifier = identifier
        self.env = env

    def accept(self, visitor):
        return vistor.visit_id(self)
    

"""        
class AstSay(AstNode):
    def __init__(self):
        self.type = "say"

    def __str__(self):
        return self.type
"""
 
