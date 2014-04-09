class Graf():
    # node_list

    def __init__(self, json=None):
        pass
        
    def push(self,node_list):
        self.node_list.append(node_list)
        
    def push_node(self,node):
        # We might not need this
        self.push([node])
    
    # TODO: Program 5