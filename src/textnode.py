from enum import Enum
class TextType(Enum):
    PLAIN = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self,text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text,
            self.text_type == other.text_type,
            self.url == other.url
        )
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"

