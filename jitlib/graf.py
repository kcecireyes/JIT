class Graf():
    def __init__(self, json=None):
    	self.node_list = []
    	self.number_of_vert = 0

    def add(self, node_list):
        self.number_of_vert += len(node_list)
    	self.node_list.extend(node_list)

    def add_edge(self, node1, node2):
        # needs work, what does it mean for 2 articles to be the same
        if node1 not in self.node_list:
            self.node_list.append(node1)
        if node2 not in self.node_list:
            self.node_list.append(node2)

        node1.add_adjacent(node2)
        node2.add_adjacent(node1)

    def contains(self, node):
        if node in self.node_list:
            return True
        else:
            return False

    def get_node(self, node):
        for i in self.node_list:
            if i == node:
                return node

    def get_node_by_title(self, title):
        for i in self.node_list:
            if i.title == title:
                return i

    def print_graf(self):
        for i in self.node_list:
            for n in i.adjacencies:
                print ("( %s , %s )" % (i.title, n.title))
