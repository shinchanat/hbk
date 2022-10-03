from css_statements import *
import element_style_generator


default_design = {
    "textSize" : "font-size : 20px;\n\t",
    "textStyle" : "font-family : 'Courier New';\n\t",
    }

class Label:

    count = 0

    def __init__(self,text = "Label",name = "label",**props):
        
        self.props = props
        self.name = name+'-'+str(Label.count) if name == "label" else name
        self.text = text
        Label.count += 1
        self.default_design = default_design

    def style_generate(self):

        return element_style_generator.generate(default_design,self)

    def self_generate(self):

        return f"""<span class = '{self.name}'>{self.text}</span>"""


if __name__ == "__main__":

    label = Label()
    print(label.style_generate())
    print(label.self_generate())
