class BoxLayout:

    count = 0

    def __init__(self,name = "boxlayout", bgColor = "transparent",alignX = "none",alignY = "none",
                 size = ("100%","100%")*2 , posMode = "relative" , pos = (None,)*2, alignBy = "column",
                 padding = {"top":"0px","right":"0px","bottom":"0px","left":"0px"},
                 margin = {"left":"0px","right":"0px","top":"0px","bottom":"0px"},
                 mode = 'flex'):

        self.name       = name+'-'+str(BoxLayout.count) if name == "boxlayout" else name
        self.alignX     = alignX
        self.alignY     = alignY
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
            "display : " + f"{self.mode};\n\t"
            "flex : 1fr;\n\t"
            "padding :" + f"{self.padding.get('top','0px')} {self.padding.get('right','0px')} {self.padding.get('bottom','0px')} {self.padding.get('left','0px')};\n\t"
            "flex-direction : "+f"{self.alignBy};\n\t"
            "align-items : "+f"{self.alignY if self.alignBy == 'row' else self.alignX};\n\t"
            "justify-content : " + f"{self.alignX if self.alignBy == 'row' else self.alignY};\n\t"
            "margin : "+f"{self.margin.get('top','0px')} {self.margin.get('right','0px')} {self.margin.get('bottom','0px')} {self.margin.get('left','0px')};\n\t"
            "background-color : " + f"{self.bgcolor};\n\t"
            "height : " + f"{self.size[-1]};\n\t"
            "width : "+f"{self.size[0]};\n\t"
            "position : "+f"{self.posMode};\n\t"
            "top : "+f"{self.pos[0]};\n\t"
            "left : "+f"{self.pos[1]};\n"
            "}"
            )

        return self.__design



if __name__ == "__main__":

    from htmltemplate import Html
    from button import Button
    from input import Input
    
    boxlayout = BoxLayout()
    btn = Button()
    btn2 = Button()
    inp = Input()
    
    component_list = [btn2,inp]
    boxlayout.addComponent(component_list)
    print(boxlayout.style_generate())

