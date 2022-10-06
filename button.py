from css_statements import *
import element_style_generator
from image import Image

# 'Default_design' is the design of the component by default.

class Button:

    count = 0
    def __init__(self,text = 'Button',name = 'button',**props):

        self.name = name+'-'+str(Button.count) if name == 'button' else name
        self.props = props
        self.text = text

        Button.count += 1
        
        self.default_design = {
            
            "bgColor" : "background-color : blue;\n\t",
            "color" : "color : white;\n\t",
            "border" : "border : none;\n\t",
            "radius" : "border-radius : 0px;\n\t",
            "padding" : "padding : 15px;\n\t",
            "position" : "position : relative;\n\t",
            "textSize" : "font-size : 17px;\n\t",
            "textStyle" : "font-style : 'Courier New';\n\t",
        }


    def style_generate(self):
        
        return element_style_generator.generate(self.default_design , self)

    def self_generate(self):
            return (f"""<div><button class = '{self.name}'>{self.text}</button></div>""")

if __name__ == "__main__":
    
    button = Button(bgColor = 'red',sizeX = 50,color = "white",topLeftRadius = 10,alignX = 104)
    print(button.self_generate())
    print(button.style_generate())
    print(Button().style_generate())
