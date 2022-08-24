class Button:

    count = 0
    def __init__(self,name = "default-button",text = "click",padding = (10,10,10,10),color = "white" ,bgcolor = "blue",
                 height = None,width = None,radius = 10,pos = ("absolute","0px","0px")):
        self.name = name+"-"+str(Button.count) if name == "default-button" else name
        self.text = text
        self.padding = padding
        self.color = color
        self.bgcolor = bgcolor
        self.height = height
        self.width = width
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
            "width : " +f"{self.width}px;\n\t"
            "position : "+f"{self.pos[0]};\n\t"
            "top : "+f"{self.pos[-1]};\n\t"
            "left : "+f"{self.pos[1]};\n\t"
            "height : " +f"{self.height}px;\n\t"
            "border : " +"none;\n\t"
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
    file = open("file.html","w")
    cssfile = open("cssfile.css","w")
    cssfile.write(button.style_generate())
    file.write(button.self_generate())
    file.close()
    cssfile.close()

##    button = Button()
##    print(button.self_generate())
##    print(button.style_generate())
##    print(button.function_generator())
##
##    button2 = Button(name = "button1" , bgcolor = "red" , text = "press",padding = (50,)*4 , color = "green")
##    print(button2.self_generate())
##    print(button2.style_generate())
##    
##    print(Button.count)
