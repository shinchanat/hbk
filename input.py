class Input:
    
    count = 0
    
    def __init__(self,name = "input-field", radius = (10,)*4,  placeholder = "Enter your text here ..",
                 border = { "color" : "black","width" : "1px","type" : "solid"},size = (None,)*2,
                 padding = {"top":"10px","right":"10px","bottom":"10px","left":"10px"},
                 margin = {"left":"10px","right":"10px","top":"10px","bottom":"10px"},
                 bgColor = "white",posMode = "relative", pos = ("0px","0px"),color = "gray",
                 mode  = "text", fontSize = "10px", fontFamily = "Courier New",length = 8,
                 ):
        
        self.radius = radius
        self.placeholder = placeholder
        self.name = name+"-"+str(Input.count) if name == "input-field" else name
        self.padding = padding
        self.size = size
        self.fontSize = fontSize
        self.fontFamily = fontFamily
        self.bgcolor = bgColor
        self.color = color
        self.posMode = posMode
        self.border = border
        self.mode = mode
        self.pos = pos
        self.margin = margin
        self.length = length
        Input.count += 1

    def style_generate(self):
        
        return ( f"\n.{self.name}"+"{\n\t"
                 "padding :" + f"{self.padding.get('top','10px')} {self.padding.get('right','10px')} {self.padding.get('bottom','10px')} {self.padding.get('left','10px')};\n\t"
                 "border-radius : "+f"{self.radius[0]}px {self.radius[1]}px {self.radius[2]}px {self.radius[3]}px;\n\t"
                 "margin : "+f"{self.margin.get('top','10px')} {self.margin.get('right','10px')} {self.margin.get('bottom','10px')} {self.margin.get('left','10px')};\n\t"
                 "background-color : " + f"{self.bgcolor};\n\t"
                 "border : "+f"{self.border['color']};\n\t"
                 "border-style : "+f"{self.border['type']};\n\t"
                 "border-width : "+f"{self.border['width']};\n\t"
                 "color : " + f"{self.color};\n\t"+
                 "height : " + f"{self.size[1]}px;\n\t"
                 "width : " + f"{self.size[0]}px;\n\t"
                 "position : "+f"{self.posMode};\n\t"
                 "top : "+f"{self.pos[0]};\n\t"
                 "left : "+f"{self.pos[1]};\n\t"
                 "font-size : "+f"{self.fontSize};\n\t"
                 "font-family : "+f"'{self.fontFamily}';\n"+"}")

    def function_grenerate(self):

        return f"""\nfunction onClick_{self.name.replace('-','_')}();"""

    def self_generate(self):
        if self.mode != "password":
            return f"""\n<input class = "{self.name}" type = "{self.mode}" placeholder = "{self.placeholder}">"""
        
        return f"""\n<input class = "{self.name}" type = "{self.mode}" placeholder = "{self.placeholder}" maxlength = {self.length}>"""


if __name__ == "__main__":

    field = Input()
    print(field.style_generate())
    print(field.self_generate())
