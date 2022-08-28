class Button:

    count = 0
    def __init__(self,name = "button",text = "Press",padding = {"top":"10px","right":"10px","bottom":"10px","left":"10px"},
                 color = "white" , bgColor = "blue",size = ("10%",)*2,radius = 10,posMode = "relative",
                 pos = ("0px","0px"),fontSize = "100%",fontFamily = "Courier New", elevation = "10px",
                 margin = {"left":"10px","right":"10px","top":"10px","bottom":"10px"}):
        
        self.name = name+"-"+str(Button.count) if name == "button" else name
        self.text = text
        self.padding = padding
        self.color = "black" if bgColor == "transparent" else color
        self.size = size
        self.posMode = posMode
        self.bgcolor = bgColor
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.radius = radius
        self.elevation = elevation
        self.margin = margin
        Button.count += 1
        self.pos = pos

    def style_generate(self):

        return (f"\n.{self.name}"+"{\
            \n\tcolor : "+f"{self.color};\n\t"
            "background-color :" + f"{self.bgcolor};\n\t"
            "padding :" + f"{self.padding.get('top','10px')} {self.padding.get('right','10px')} {self.padding.get('bottom','10px')} {self.padding.get('left','10px')};\n\t"
            "width : " +f"{self.size[0]};\n\t"
            "position : "+f"{self.posMode};\n\t"
            "top : "+f"{self.pos[0]};\n\t"
            "margin : "+f"{self.margin.get('top','10px')} {self.margin.get('right','10px')} {self.margin.get('bottom','10px')} {self.margin.get('left','10px')};\n\t"
            "left : "+f"{self.pos[1]};\n\t"
            "height : " +f"{self.size[1]};\n\t"
            "border : " +"none;\n\t"
            "font-size : "+f"{self.fontSize};\n\t"
            "box-shadow : "+f"0px 0px {self.elevation} grey;\n\t"
            "font-family : "+f"'{self.fontFamily}';\n\t"
            "border-radius : " +f"{self.radius}px;"+"\n}\n"\
            +f".{self.name}:hover"+"{\n"
            +"\t opacity : 0.7;\n"+"}\n"

            +f".{self.name}:active"+"{\n"
            +"\t opacity : 0.5;\n"+"}"
            
            )

    def function_generate(self):

        return f"""\nfunction onClick_{self.name.replace('-','_')}()"""+"{\n\tconsole.log(\"clicked\");\n}"

    def self_generate(self):

        return (f"""\n<button class = "{self.name}">{self.text}</button>""")

if __name__ == "__main__":

    button = Button()

    print(button.self_generate())

    print(button.style_generate())

