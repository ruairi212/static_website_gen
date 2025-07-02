import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_multiple_props(self):
        node = HTMLNode(
            tag='a',
            value='click me!',
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
                ' href="https://www.google.com" target="_blank"'
            
        )