#Not reday for use .
#boxlayout all the boxlayout object.

from css_statements import *
from boxlayout import BoxLayout
from label import Label
from image import Image
import element_style_generator

class ListItem:

    count = 0
    
    def __init__(self,icon = None,divider = False , text = 'ListItem',name = 'list-item',**props):
        
        self.name = name+'-'+str(ListItem.count) if name == 'list-item' else name
        self.props = props
        self.text = text
        self.icon = icon
        self.layout = BoxLayout([Image(self.icon,margin = 10,radius = '50px'),
                                 Label(self.text,)],alignBy = 'row',align = 'center',bgColor = 'white',sizeY = '80px')
        self.hover_design = {"bgColor" : "rgb(246, 243, 243)",}
        self.active_design = {"opacity" : "0.5",}
        ListItem.count += 1
        self.default_design = {}#self.layout.get_default_design()
        self.divider = divider

    def style_generate(self):

        css = self.layout.style_generate()
        
        #self.default_design.update(self.layout.get_default_design()) #get the default design of boxlayout and update to self.default_design.
        #css += element_style_generator.generate(self.default_design,self)+'\n'

        css += element_style_generator.generate_hover(self.hover_design,self.layout)+'\n'#generates a css code for hover effect.
        css += element_style_generator.generate_active(self.active_design,self.layout)+'\n'#generates a css code for active effect.

        return css

    def self_generate(self):

        return self.layout.self_generate()+f"""<div {'style = "background-color : grey;height : 1px"' if self.divider else ''}></div>"""
    


if __name__ == "__main__":

    listItem = ListItem()
    print(listItem.style_generate())

    #print(ListItem(bgColor = 'blue').style_generate())
