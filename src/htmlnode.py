class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        # string representing the the HTML tag name
        self.tag = tag
        # A string representing the value of the HTML tag
        self.value = value
        # A list of HTML objects representing the children of this node
        self.children = children
        # A dictionary of key-value pairs representing the attributes of the
        # HTML tag
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf Nodes must have values")

        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super.__init__(tag, None, children, props)

    def to_html(self):
