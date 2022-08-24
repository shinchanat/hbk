class Button:

    count = 0
    def __init__(self,name = "default-button",text = "BUTTON",padding = (10,)*4,
                 color = "white" ,bgcolor = "blue",size = (None,)*2,radius = 10,
                 posMode = "absolute",pos = ("0px","0px"),fontSize = "10px",
                 fontFamily = "Courier New"):
        
        self.name = name+"-"+str(Button.count) if name == "default-button" else name
        self.text = text
        self.padding = padding
        self.color = color
        self.size = size
        self.posMode = posMode
        self.bgcolor = bgcolor
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.radius = radius
        self.buttonCount()
        self.pos = pos


    def buttonCount(self):
        Button.count +=1

    def style_generate(self):

        return (f".{self.name}"+"{\
            \n\tcolor : "+f"{self.color};\n\t"
            "background-color :" + f"{self.bgcolor};\n\t"
            "padding :" + f"{self.padding[0]}px {self.padding[1]}px {self.padding[2]}px {self.padding[3]}px;\n\t"
            "width : " +f"{self.size[0]}px;\n\t"
            "position : "+f"{self.posMode};\n\t"
            "top : "+f"{self.pos[0]};\n\t"
            "left : "+f"{self.pos[1]};\n\t"
            "height : " +f"{self.size[1]}px;\n\t"
            "border : " +"none;\n\t"
            "font-size : "+f"{self.fontSize};\n\t"
            "font-family : "+f"'{self.fontFamily}';\n\t"
            "border-radius : " +f"{self.radius}px;"+"\n}\n"\
            +f".{self.name}:hover"+"{\n"
            +"\t opacity : 0.7;\n"+"}\n"

            +f".{self.name}:active"+"{\n"
            +"\t opacity : 0.5;\n"+"}"
            
            )

    def function_generate(self):

        return f""" function onClick_{self.name.replace('-','_')}()"""+"{\n\tconsole.log(\"clicked\");\n}"

    def self_generate(self):

        return (f"""<button class = "{self.name}">{self.text}</button>""")

if __name__ == "__main__":

    button = Button()

    print(button.self_generate())

    print(button.style_generate())

