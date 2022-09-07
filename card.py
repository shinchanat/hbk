class Card:

    count = 0

    def __init__(self,name = "card",component = [],size = ('none',)*2,align = {'x':'none','y':'none'},
                 bgColor = "white",elevation = "10px",pos = {'x':'none','y':'center'},alignBy = 'column',
                 posMode = 'relative',radius = ['10px']*4,margin = ['10px']*4,padding = ['10px']*4):
        

        self.name = name+'-'+str(Card.count) if name == "card" else name
        Card.count += 1
        self.bgColor = bgColor
        self.align = align
        self.margin = margin
        self.alignBy = alignBy
        self.component = component
        self.size = size
        self.posMode = posMode
        self.pos = pos
        self.radius = radius
        self.elevation = elevation
        self.padding = padding


    def style_generate(self):
        """position """

        style = (
            f'.{self.name}'+'{\n\t'
            f'background-color : {self.bgColor};\n\t'
            f'box-shadow : 0px 0px {self.elevation} grey ;\n\t'
            'display :'+f'flex;\n\t'
            'flex : '+f'1fr;\n\t'
            f"margin : {' '.join(self.radius)};\n\t"
            f'flex-direction : {self.alignBy};\n\t'
            f'align-items : {self.align.get("y","none") if self.alignBy == "row" else self.align.get("x","none")};\n\t'
            f'justify-content : {self.align.get("x","none") if self.alignBy == "row" else self.align.get("y","none")};\n\t'
            f'position : {self.posMode};\n\t'
            f'top : {self.pos.get("y","none")};\n\t'
            f'left : {self.pos.get("x","none")};\n\t'
            f'height : {self.size[-1]};\n\t'
            f'width : {self.size[0]};\n\t'
            f'padding : {" ".join(self.radius)};\n\t'
            f'border-radius : {" ".join(self.radius)};\n'
            '}\n\n'
            f'.{self.name}:hover'+'{\n\t'
            'background-color : rgb(246, 244, 244) ;\n'
            '}\n')

        for component in self.component:
            style += component.style_generate()

        return style

    def self_generate(self):

        return f"<div class = {self.name}>"+'\n'.join([component.self_generate() for component in self.component])+'\n</div>'


if __name__ == "__main__":

    from label import Label
    from button import Button
    from boxlayout import BoxLayout

    boxlayout = BoxLayout()

    ll = Label()
    button = Button()
    boxlayout.addComponent([ll,button])
    card = Card(component = [boxlayout])
    print(card.style_generate())
    input()


