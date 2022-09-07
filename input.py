class Input:
    
    count = 0
    
    def __init__(self,name = "input-field", radius = ['10px']*4,placeHolder = "Enter your text here ..",
                 border = { "color" : "none","width" : "1px","type" : "solid"},size = ('none',)*2,
                 padding = ['10px']*4,margin = ['10px']*4,bgColor = "transparent",posMode = "relative",
                 pos = ['0px']*2,color = "black",mode  = "text", fontSize = "100%",
                 fontStyle = "Courier New",length = 8):
        
        self.radius = radius
        self.placeHolder = placeHolder
        self.name = name+"-"+str(Input.count) if name == "input-field" else name
        self.padding = padding
        self.size = size
        self.fontSize = fontSize
        self.fontStyle = fontStyle
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
                 f"padding : {' '.join(self.padding)};\n\t"
                 f"border-radius : { ' '.join(self.radius)};\n\t"
                 f"margin : {' '.join(self.margin)};\n\t"
                 f"background-color : {self.bgcolor};\n\t"
                 f"border : {self.border['color']};\n\t"
                 "border-bottom : 1px solid silver;\n\t"
                 f"border-width : {self.border['width']};\n\t"
                 f"color : {self.color};\n\t"
                 f"height : {self.size[1]}px;\n\t"
                 f"width : {self.size[0]}px;\n\t"
                 f"position : {self.posMode};\n\t"
                 f"top : {self.pos[1]};\n\t"
                 f"left : {self.pos[0]};\n\t"
                 "outline : none;\n\t"
                 f"font-size : {self.fontSize};\n\t"
                 f"font-family : '{self.fontStyle}';\n"+"}\n\n")

    def function_grenerate(self):

        return f"""\nfunction onClick_{self.name.replace('-','_')}();"""

    def self_generate(self):
        mode = ('password','radio','date','text','checkbox','week','month')
        if not self.mode in mode:
            raise Exception('Invalid mode "{self.mode}" for input exception.')
        
        if self.mode != "password":
            
            return f"""\n<input class = "{self.name}" type = "{self.mode}" placeholder = "{self.placeHolder}">"""
        
        return f"""\n<input class = "{self.name}" type = "{self.mode}" placeholder = "{self.placeHolder}" maxlength = {self.length}>"""


if __name__ == "__main__":

    field = Input()
    print(field.style_generate())
    print(field.self_generate())
