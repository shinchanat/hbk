from css_statements import *
import element_style_generator

class ScrollLayout:

    count = 0
    def __init__(self,name = 'swiper',**props):
        self.name = name+'-'+str(ScrollLayout.count) if name == "swiper" else name
        self.props = props
        ScrollLayout.count += 1
        self.default_design = {
            "layoutMode" : "display : flex;\n\t",
            "alignBy" : "flex-direction : column;\n\t",
            "sizeY" : "height : 100%;\n\t",
            "scrollY" : "overflow-y : auto;\n\t",
        }
        self.components = []

    def style_generate(self):

        css = ""
        
        for component in self.components:
            css += element_style_generator.generate(component.default_design,component)+'\n' # generates css for child components

        css += element_style_generator.generate(self.default_design,self)+'\n'#generates css code for parent component.
        

        return css
        

    def addComponent(self,components):
        self.components = components

    def self_generate(self):

        return f"<div class = '{self.name}'>\n"+'\n\t'.join([comp.self_generate() for comp in self.components])+'\n</div>'


if __name__ == "__main__":


    print(ScrollLayout(sizeY = 90).style_generate())
    print(ScrollLayout().style_generate())
