class Label:

    count = 0

    def __init__(self,name = "label",text = "hyperlinked-bilang-kit",fontSize = "10px",
                 fontFamily = 'Courier New',color = "black",bgColor = "transparent",
                 pos = ("0px","0px"),posMode = "relative"):

        self.name = name+'-'+str(Label.count) if name == "label" else name
        self.text = text
        self.pos = pos
        self.posMode = posMode
        self.fontSize = fontSize
        self.fontFamily = fontFamily
        self.color = color
        self.bgColor = bgColor
        self.count += 1

    def style_generate(self):

        return (f".{self.name}"+"{\n\t"
                "color : "+f"{self.color};\n\t"
                "font-size : "+f"{self.fontSize};\n\t"
                "font-family :"+f"{self.fontFamily};\n\t"
                "display : inline-block;\n\t"
                "position : "+"{self.posMode};\n\t"
                "top : "+f"{self.pos[1]};\n\t"
                "left : "+f"{self.pos[0]};\n\t"
                "background-color : "+f"{self.bgColor};\n"
                "}")

    def self_generate(self):

        return f"<p class = '{self.name}'>{self.text}</p>"

    def function_generate(self):

        return f"function {self.name}();"


if __name__ == "__main__":

    label = Label()

    print(label.self_generate())
    

    print(label.style_generate())
