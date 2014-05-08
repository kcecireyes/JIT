import unittest
from node import *
from graf import *
from collection import *


class TextJIT(unittest.TestCase):
    def setUp(self):
    	pass

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
        self.assertEqual(node.keywords[2], "hip")
        self.assertEqual(node.keywords[0], "awesome")
        # can add single strings
        node.add_keywords("the best")
        self.assertEqual(node.keywords[4], "the best")

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

    def test_should_create_empty_collection(self):
        collection = Collection()
        self.assertIsInstance(collection, Collection)

    def test_should_create_loaded_collection(self):
        node = Node()
        node1 = Node()
        collection = Collection([node, node1])
        self.assertEqual(collection.len, 2)

    def test_collection_should_add_nodes(self):
        collection = Collection()
        node = Node()
        collection.add_node(node)
        self.assertEqual(collection.len, 1)

    def test_should_create_empty_graf(self):
        graf = Graf()
        self.assertIsInstance(graf, Graf)

    def test_graf_should_add_nodes(self):
        graf = Graf()
        node = Node()
        graf.push_node(node)
        self.assertEqual(graf.number_of_vert, 1)

    def test_graf_should_add_collection(self):
        graf = Graf()
        node = Node()
        node1 = Node()
        node2 = Node()
        node3 = Node()
        collection = Collection([node1, node2])
        graf.push_node(node)
        graf.push_node(node3)
        graf.push_collection(collection)
        self.assertEqual(graf.number_of_vert, 4)

    def test_graf_should_get_node(self):
        graf = Graf()
        node = Node()
        graf.push_node(node)
        node.title = "title"
        self.assertIs(node, graf.get_node_by_title("title"))

    def test_graf_method_contains(self):
        graf = Graf()
        node = Node()
        graf.push_node(node)
        self.assertTrue(graf.contains(node))

    def test_graf_add_edge(self):
        graf = Graf()
        node = Node()
        node2 = Node()
        graf.push_node(node)
        graf.push_node(node2)
        graf.add_edge(node, node2)
        self.assertEqual(graf.get_node(node).adjacencies()[0], node2)

if __name__ == '__main__':
    unittest.main()
