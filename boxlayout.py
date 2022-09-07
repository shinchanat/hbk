class BoxLayout:

    count = 0

    def __init__(self,name = "boxlayout", bgColor = "transparent",align = {'x':'none','y':'none'},
                 size = ["100%"]*2 , posMode = "relative" , pos = ['none',]*2, alignBy = "column",
                 radius = ['0px']*4,padding = ['0px']*4,elevation = False ,margin = ['0px']*4,
                 mode = 'flex'):

        self.name       = name+'-'+str(BoxLayout.count) if name == "boxlayout" else name
        self.align      = align
        self.bgcolor    = bgColor
        self.size       = size
        self.padding    = padding
        self.posMode    = posMode
        self.pos        = pos
        self.margin     = margin
        self.alignBy    = alignBy
        self.mode       = mode
        self.__layout   = ""
        self.__design   = ""
        BoxLayout.count += 1
        self.radius = radius
        self.elevation = elevation

    def self_generate(self):

        return self.__layout

    def addComponent(self,component):
        
        for comp in component:
            self.__design += comp.style_generate()

        self.__layout = f"\n<div class = '{self.name}'>\n\t"+'\n'.join([ comp.self_generate() for comp in component])+"\n</div>"

        #return self.__layout


    def style_generate(self):

        self.__design += (
            f"\n.{self.name}" + "{\n\t"
            f"display : {self.mode};\n\t"
            "flex : 1fr;\n\t"
            f"border-radius : {' '.join(self.radius)};\n\t"
            f"padding :{' '.join(self.padding)};\n\t"
            f"flex-direction : {self.alignBy};\n\t"
            f"align-items : {self.align.get('y','none') if self.alignBy == 'row' else self.align.get('x','none')};\n\t"
            f"justify-content : {self.align.get('x','none') if self.alignBy == 'row' else self.align.get('y','none')};\n\t"
            f"margin : {' '.join(self.margin)};\n\t"
            f"background-color : {self.bgcolor};\n\t"
            f"height : {self.size[-1]};\n\t"
            f"width : {self.size[0]};\n\t"
            f"position :{self.posMode};\n\t"
            f"top : {self.pos[0]};\n\t"
            f"left : {self.pos[1]};\n\t"
            f"box-shadow : {'none' if self.elevation == False else '0px 0px 10px grey'};\n"
            "}"
            )

        return self.__design



if __name__ == "__main__":

    from htmltemplate import Html
    from button import Button
    from input import Input
    
    boxlayout = BoxLayout(elevation = False)
    btn = Button()
    btn2 = Button()
    inp = Input()
    
    component_list = [btn2,inp]
    boxlayout.addComponent(component_list)
    print(boxlayout.self_generate())
    print(boxlayout.style_generate())
    input()

