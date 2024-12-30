class HTMLNode():
    def __init__(self, tag=None, value=None , children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        props_value = ""#.join(f'{name}={value}')
        for key, value in self.props.items():
            props_value += f' {key}="{value}"'
        return props_value
    
    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children},props={self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        if self.children:
            raise ValueError("LeafNode cannot have children")
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>' #call HTMLNode method to evaluate the props.

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        if self.value :
            raise ValueError("ParentNode cannot have value")
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        
        html_str = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html_str += child.to_html()
        html_str += f'</{self.tag}>'

        return html_str

        