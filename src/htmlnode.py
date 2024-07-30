Class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        #string representing the the HTML tag name
        self.tag = tag
        #A string representing the value of the HTML tag
        self.value = value
        #A list of HTML objects representing the children of this node
        self.children = children
        #A dictionary of key-value pairs representing the attributes of the HTML tag
        self.props = props

    def to_html(self):
        raise NotImplementedError()


    def props_to_html(self):
        new_string = ""
        for prop in self.props:
            newstring += f" href=\"{prop}\" target=\"{props[prop}\""
        return new_string

    def __repr__(self):

