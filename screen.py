class Screen:

    count = 0

    def __init__(self,name = 'root',background = 'white',justify = 'none',align = 'none'):
        self.name = name+'-'+str(Screen.count) if name == 'root' else name
        self.background = background
        self.justify = justify
        self.align = align
        Screen.count += 1
        self.__layout = ''
        self.__design = (f".{self.name}""{\n\t"
                "margin : 0px;\n\t"
                "padding : 0px;\n\t"
                f"justify-content : {self.justify};\n\t"
                f"align-items : {self.align};\n""}\n")

    def style_generate(self):

        return self.__design

    def self_generate(self):

        return self.__layout

    def addComponent(self,component):
        
        for comp in component:
            self.__design += comp.style_generate()

        self.__layout = f"\n<body class = '{self.name}' style = 'display : flex; flex : 1fr; flex-direction : column; background : {self.background}; flex : 1; alignItems : 'center';'>\n\t"+'\n'.join(
            [ comp.self_generate() for comp in component])+"\n</body></html>"


if __name__ == "__main__":

    from label import Label
    from boxlayout import BoxLayout
    

    screen = Screen()
    view1 = BoxLayout()
    view1.addComponent([Label(text = 'boxlayout')])
    screen.addComponent([Label(text = 'view1'),view1])
    print(screen.style_generate())
    print(screen.self_generate())
        
