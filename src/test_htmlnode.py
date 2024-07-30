import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest, HTMLNode):
    def test_eq(self):

        node = HTMLNode("h1", "this is some test text")
        node1 = HTMLNode("p", "more test text", None, {"href": "https://www.google.com"})
        print(node)
        node2_prop = node1.props_to_html()

        print(node2_prop)

if __name__ == "__main__":
    unittest.main()