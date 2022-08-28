import webbrowser

class Html:
    
    def __init__(self,filename,root = None):
        self.root = root
        self.filename = filename
        self.template = (
            f"""<html>\n\t<head>\n\t\t<title></title>\n\t\
        <link rel = "stylesheet" href = "{self.filename.replace('html','css')}">\n\t</head>\
            \n<body style = 'display : flex; flex : 1fr; margin : 0px;'>\n\t{root.self_generate()}\n</body>\n</html>"""
            )

    def save(self):
        with open(f'{self.filename}','w') as htmlfile:
            htmlfile.write(self.template)

        with open(f'{self.filename.replace(".html",".css")}','w') as cssfile:
            cssfile.write(self.root.style_generate())

        webbrowser.open(f'{self.filename}')
## development testing section

if __name__ == "__main__":

    from boxlayout import BoxLayout
    from input import Input
    from button import Button
    from label import Label

    layout = BoxLayout(alignY = "center")
    titlelayout = BoxLayout(alignX = "center",alignY = "center",size = ("100%","10%"))
    titlelayout.addComponent([Label(text = "We are from pyWeb community.",elevation = "2px")])
    layout.addComponent(
        [
         titlelayout,
         Input(placeholder = "Username "),
         Input(placeholder = "Password "),
         Button(text = "Press",size = ("90s%",None))
        ]
    )

    Html('testing.html',layout).save()
##    print(layout.self_generate())
##    print(layout.style_generate())
