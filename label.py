class Label:

    count = 0

    def __init__(self,name = "label",text = "Text",fontSize = "100%",
                 fontStyle = 'Courier New',color = "black",bgColor = "transparent",
                 align = {'x':'none','y':'none'},posMode = "relative",elevation = 'none',
                 padding = ['0px']*4,margin = ['0px']*4):

        self.name = name+'-'+str(Label.count) if name == "label" else name
        self.text = text
        self.align = align
        self.margin = margin
        self.padding = padding
        self.posMode = posMode
        self.fontSize = fontSize
        self.fontStyle = fontStyle
        self.color = color
        self.bgColor = bgColor
        self.elevation = elevation
        Label.count += 1

    def style_generate(self):

        return (f".{self.name}"+"{\n\t"
                f"color : {self.color};\n\t"
                f"text-align : {self.align.get('x','none')};\n\t"
                f"font-size : {self.fontSize};\n\t"
                f"font-family : {self.fontStyle};\n\t"
                f"font-weight : bold;\n\t"
                "display : inline-block;\n\t"
                f"position : {self.posMode};\n\t"
                f"padding  : {' '.join(self.padding)};\n\t"
                f"margin : {' '.join(self.margin)};\n\t"
                f"top : {self.align.get('y','none')};\n\t"
                f"left : {self.align.get('x','none')};\n\t"
                f"text-shadow : 0px 0px {self.elevation} grey;\n\t"
                f"background-color : {self.bgColor};\n"
                "}")

    def self_generate(self):

        return f"\n<p class = '{self.name}'>{self.text}</p>"

    def function_generate(self):

        return f"function {self.name}();"


if __name__ == "__main__":

    label = Label()

    print(label.self_generate())
    

    print(label.style_generate())
