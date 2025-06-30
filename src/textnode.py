from enum import Enum
class TextType(Enum):
    TEXT_PLAIN = "text"
    TEXT_BOLD = "bold"
    TEXT_ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGES = "images"

class Textnode:
    def __init__(self,text, text_type, url):
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
        return f"Textnode({self.text},{self.text_type.value},{self.url})"

