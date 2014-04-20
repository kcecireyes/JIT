class Graf():
    def __init__(self, json=None):
    		self.node_list = []
    		self.number_of_vert = 0
    
    def push(self, node_list):
    		self.number_of_vert += node_list.length
    		self.node_list.extend(node_list)
    
    def push_node(self,node):
        # We might not need this
        self.number_of_vert += 1
        self.append(node)
