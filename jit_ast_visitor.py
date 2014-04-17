class AstVisitor:
    def visit_fun(self, fun_node):
        if fun_node.subtype == "say":
            return "\n".join(str(st) for st in fun_node.params)
