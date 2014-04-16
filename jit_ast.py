class AstNode: pass

class AstBinOp(AstNode):
    def __init__(self,left,op,right):
        self.type = "binop"
        self.left = left
        self.right = right
        self.op = op
        
    def to_string(self):
        return self.left.to_string + self.op.to_string + self.right.to_string

class AstFun(AstNode):
    def __init__(self,subtype):
        self.type = "function"
        self.subtype = subtype
        # self.child

    def to_string(self):
        return self.subtype + "\n" + self.child.to_string()

class AstString(AstNode):
    def __init__(self,value):
        self.type = "string"
        self.value = value

    def to_string(self):
        return self.value

class AstSay(AstNode):
    def __init__(self):
        self.type = "say"

    def to_string(self):
        return self.type

