class Input:
    count = 0
    def __init__(self,name = "default-input-field",radius = (10,)*4,
                 placeholder = "Enter your text here ..",
                 size = (None,)*2, padding = (10,)*4,
                 bgcolor = "white",posMode = "absolute",
                 pos = ("0px","0px"),color = "gray", mode  = "text",
                 fontSize = "10px", fontFamily = "Courier New"
                 ,
                 ):
        
        self.radius = radius
        self.placeholder = placeholder
        self.name = name+"-"+str(Input.count) if name == "default-input-field" else name
        self.padding = padding
        self.size = size
        self.fontSize = fontSize
        self.fontFamily = fontFamily
        self.bgcolor = bgcolor
        self.color = color
        self.posMode = posMode
        self.mode = mode
        self.pos = pos
        Input.count += 1

    def style_generate(self):
        
        return ( f".{self.name}"+"{\n"
                 "\tpadding : " + f"{self.padding[0]}px {self.padding[1]}px {self.padding[2]}px {self.padding[2]}px;\n\t"
                 "border-radius : "+f"{self.radius[0]}px {self.radius[1]}px {self.radius[2]}px {self.radius[3]}px;\n\t"
                 "background-color : " + f"{self.bgcolor};\n\t"
                 "border : none;\n\t"
                 "color : " + f"{self.color};\n\t"+
                 "height : " + f"{self.size[1]}px;\n\t"
                 "width : " + f"{self.size[0]}px;\n\t"
                 "position : "+f"{self.posMode};\n\t"
                 "top : "+f"{self.pos[0]};\n\t"
                 "left : "+f"{self.pos[1]};\n\t"
                 "font-size : "+f"{self.fontSize};\n\t"
                 "font-family : "+f"'{self.fontFamily};'\n"+"}")

    def function_grenerate(self):

        return f""" function onClick_{self.name.replace('-','_')}();"""

    def self_generate(self):
        return f"""<input class = "{self.name}" type = "{self.mode}" placeholder = "{self.placeholder}">"""


if __name__ == "__main__":

    field = Input()
    print(field.style_generate())
   # with open("inputfiled.html","w") as htmlfile:
      #  htmlfile.write(field.self_generate())
    print(field.self_generate())
