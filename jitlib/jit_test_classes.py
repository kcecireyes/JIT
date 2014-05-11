import unittest
from node import *
from graf import *
from database import Base, engine

class TextJIT(unittest.TestCase):
    def setUp(self):
    	Base.metadata.create_all(engine)

    def test_for_the_sake_of_testing(self):
        s = "blah"
    	self.assertEqual(s, "blah")
    	self.assertEqual((2 + 2), 4)

    def test_should_create_blank_node(self):
    	node = Node()
    	self.assertIsInstance(node, Node)

    def test_should_create_node_with_fields(self):
        node = Node("title", "author", "publisher", "body")
        self.assertIsInstance(node, Node)
        self.assertEqual(node.title, "title")
        self.assertEqual(node.author, "author")
        self.assertEqual(node.publisher, "publisher")
        self.assertEqual(node.body, "body")

    def test_nodes_should_add_fields(self):
        node = Node()
        node.title = "i am a title"
        node.author = "Raul Matias"
        node.publisher = "I am the publisher"
        self.assertEqual(node.author, "Raul Matias")
        self.assertEqual(node.title, "i am a title")
        self.assertEqual(node.publisher, "I am the publisher")

    def test_nodes_should_add_keywords(self):
        node = Node()
        # can add lists
        node.add_keywords(["awesome", "cool", "hip", "great"])
        self.assertEqual(node.keywords[2], Keyword("hip"))
        self.assertEqual(node.keywords[0], Keyword("awesome"))
        # can add single strings
        node.add_keywords("the best")
        self.assertEqual(node.keywords[4], Keyword("the best"))

    def test_nodes_should_add_body(self):
        node = Node()
        # can add single string
        node.add_body("I am a small body.")
        self.assertEqual(node.body, "I am a small body.")
        # can add text file
        node.add_body("test_body.txt", "f")
        self.assertEqual(node.body, "I am a large body." )

    def test_nodes_should_add_adjacent(self):
        node1 = Node()
        node2 = Node()
        node1.add_adjacent(node2)
        self.assertIs(node1.adjacencies()[0], node2)

    def test_should_create_empty_graf(self):
        graf = Graf()
        self.assertIsInstance(graf, Graf)

    def test_graf_should_add_nodes(self):
        graf = Graf()
        node = Node()
        graf.add(node)
        self.assertEqual(len(graf.nodes), 1)

    def test_graf_should_get_node(self):
        graf = Graf()
        node = Node()
        graf.add(node)
        node.title = "title"
        self.assertIs(node, graf.get_node_by_title("title"))

    def test_graf_method_contains(self):
        graf = Graf()
        node = Node()
        graf.add(node)
        self.assertTrue(graf.contains(node))

    def test_graf_add_edge(self):
        graf = Graf()
        node = Node()
        node2 = Node()
        graf.add(node, node2)
        graf.add_edge(node, node2)
        self.assertEqual(graf.get_node(node).adjacencies()[0], node2)

    def test_graf_pull(self):
        node = Node()
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()

        node1.add_adjacencies(node2,node3)
        node3.add_adjacencies(node4)

        graf1 = Graf()
        graf2 = Graf()
        graf3 = Graf()

        graf1.add(node1, node2, node3, node4)
        graf1.push()

        graf2 = pull(node1, 3)
        graf3 = pull(node1, 4)

        self.assertEqual(len(graf2.nodes), 3)
        self.assertEqual(len(graf3.nodes), 4)

        self.assertTrue(node4 not in graf2.nodes)
        self.assertTrue(node4 in graf3.nodes)

    def test_graf_search(self):
        node = Node()
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        graf = Graf()

        node1.author = "node1 author"
        node1.add_keywords(["node1", "a node", "test"])
        node2.author = "node1 author"
        node2.add_keywords(["node3", "test"])
        node3.author = "node3 author"
        node3.publisher = "node3 publisher"
        node4.author = "node4 author"
        node4.publisher = "node publisher"

        graf.add(node1, node2, node3, node4)
        graf.push

        graf2 = search(keywords="test")

        self.assertEqual(node1 in graf.nodes)
        self.assertEqual(node2 in graf.nodes)
        self.assertEqual(node3 not in graf.nodes)


if __name__ == '__main__':
    unittest.main()
