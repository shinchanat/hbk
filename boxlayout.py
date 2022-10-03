from css_statements import *
import element_style_generator

default_design = {
    
    "bgColor" : "background-color : white;\n\t",
    "posMode" : "position : relative;\n\t",
    "alignBy" : "flex-direction : column;\n\t",
    }

class BoxLayout:

    count = 0
    
    def __init__(self,components = [],name = "boxlayout",**props):
        
        self.name = name+'-'+str(BoxLayout.count) if name == "boxlayout" else name
        self.components = components
        self.props = props
        self.default_design = default_design
        BoxLayout.count += 1

    def style_generate(self):

        css = ""
        
        for component in self.components:
            css += element_style_generator.generate(component.default_design,component)+'\n' # generates css for child components

        css += element_style_generator.generate(default_design,self)+'\n'#generates css code for parent component.
        

        return css

    def self_generate(self):

        return f"<div class = '{self.name}' style = 'display : flex; flex : 1fr;'>\n\t"+"\n\t".join([component.self_generate() for component in self.components])+"\n</div>"


if __name__ == "__main__":


    from button import Button
    from input import Input
    from label import Label

    boxlayout = BoxLayout([Button(),BoxLayout()],bgColor = 'red')
    print(boxlayout.style_generate())
    print(boxlayout.self_generate())
    
        
        
