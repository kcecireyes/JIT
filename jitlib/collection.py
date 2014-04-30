class Collection():
    # node_list
    
    def __init__(self, node_list=None):
        if node_list:
            self.node_list = node_list
            self.len = len(node_list)
        else:
        		self.node_list = []
        		self.len = 0

    def add_node(self, node):
    		self.node_list.append(node)
    		self.len += 1

    def get_nodes(self):
    		return self.node_list

    def contains(self, node):
    		if node in self.node_list:
    				return True
    		else:
    				return False

    def to_json(self):
        pass
