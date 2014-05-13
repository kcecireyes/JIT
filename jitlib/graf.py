from database import session

def search(number=None, keywords=[], author=None, publisher=None):
    from node import Node, Keyword
    query = session.query(Node)

    if author != None:
        query = query.filter(Node.author == author)

    if publisher != None:
        query = query.filter(Node.publisher == publisher)

    query = query.all()

    # if there are any keywords, only include nodes which are
    # tagged with one of those keywords
    if len(keywords) > 0:
        keyword_nodes = []
        for keyword in keywords:
            keyword_obj = Keyword(keyword)
            keyword_nodes.extend(keyword_obj.nodes)

        keyword_nodes = set(keyword_nodes)
        query = set(query)
        final = query.intersection(keyword_nodes)
    else:
        final = query

    # Add all nodes, but not more than the number if specified.
    graf = Graf()
    if number != None:
        for node in final[:number]:
            graf.add(node)
    else:
        for node in final:
            graf.add(node)

    return graf

def pull(node=None, number=0):
    remaining = number
    graf = Graf()

    if node == None or number == 0:
        return graf

    ring = [node]

    while len(graf.nodes) < number and len(ring) > 0:
        # Add all the nodes in the current ring
        # that will fit in the graph.
        for node in ring:
            if len(graf.nodes) < number:
                graf.add(node)

        if len(graf.nodes) > 0 and len(graf.nodes) < number:
            # Get all children
            children = []
            for node in ring:
                children.extend(node.adjacencies())

            # Remove duplicates
            children = list(set(children))

            # Only if it isn't already in our graph
            ring = [node for node in children if node not in graf.nodes]

    return graf

class Graf():
    def __init__(self, json=None):
    	self.nodes = []

    def push(self):
        session.add_all(self.nodes)
        session.commit()

    def add(self, *nodes):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)

    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)

        node1.add_adjacent(node2)

    def contains(self, node):
        if node in self.nodes:
            return True
        else:
            return False

    def get_node(self, node):
        for i in self.nodes:
            if i == node:
                return node

    def get_node_by_title(self, title):
        for i in self.nodes:
            if i.title == title:
                return i

    def print_graf(self):
        for i in self.nodes:
            for n in i.adjacencies:
                print ("( %s , %s )" % (i.title, n.title))
