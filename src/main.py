from textnode import Textnode
from textnode import TextType
def main():
    node = Textnode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
if __name__ == "__main__":
    main()