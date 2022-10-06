from css_statements import *
import element_style_generator

class Input:

    count = 0

    def __init__(self,placeHolder = "Enter your text here...",name = "input",mode = "text",**props):

        self.name = name+'-'+str(Input.count) if name == "input" else name
        self.props = props
        self.placeHolder = placeHolder
        self.mode = mode
        Input.count += 1
        self.default_design = {

            "bgColor" : "background-color : transparent;\n\t",
            "padding" : "padding : 15px;\n\t",
            "border" : "border : none;\n\t",
            "textSize" : "font-size : 17px;\n\t",
            "textStyle" : "font-family : 'Courier New';\n\t",
            "focus" : "outline : none;\n\t",
        }

    def style_generate(self):

        return element_style_generator.generate(self.default_design,self)

    def self_generate(self):

        modes = ('text','password','date','month','radio','checkbox','file','image','week')

        if 'password' in self.placeHolder.lower():
            return f"""<div><input type = 'password' class = '{self.name}' placeHolder = '{self.placeHolder}' /></div>"""

        if self.mode in modes:
                return f"""<div><input type = '{self.mode}' class = '{self.name}' placeholder = '{self.placeHolder}' /></div>"""
        
        
        return f"""<div><input type = '{self.mode}' class = '{self.name}' placeholder = '{self.placeHolder}' /></div>"""
        


if __name__ == "__main__":

    test_input = Input(placeHolder='enter your Password : ')
    print(test_input.style_generate())
    print(test_input.self_generate())

    print(Input().style_generate())

