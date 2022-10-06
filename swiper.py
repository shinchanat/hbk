from css_statements import *
import element_style_generator


default_design = {
    "layoutMode" : "display : flex;\n\t",
    "alignBy" : "flex-direction : row;\n\t",
    "sizeY" : "height : 50%;\n\t",
    "scrollX" : "overflow-x : auto;\n\t",
    }

class Swiper:

    count = 0
    def __init__(self,name = 'swiper',**props):
        self.name = name+'-'+str(Swiper.count) if name == "swiper" else name
        self.props = props
        Swiper.count += 1
        self.default_design = default_design
        self.components = []

    def style_generate(self):

        css = ""
        
        for component in self.components:
            css += element_style_generator.generate(component.default_design,component)+'\n' # generates css for child components

        css += element_style_generator.generate(default_design,self)+'\n'#generates css code for parent component.
        

        return css
        

    def addComponent(self,components):
        self.components = components

    def self_generate(self):

        return f"<div class = '{self.name}'>\n"+'\n\t'.join([comp.self_generate() for comp in self.components])+'\n</div>'



if __name__ == '__main__':

    from button import Button
    from input import Input

    carousel = Swiper()
    carousel.addComponent([Input(),Button(),Button()])
    print(carousel.style_generate())
