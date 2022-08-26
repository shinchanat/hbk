class Html:
    
    def __init__(self,root = None):
        self.template = (
            f"""<html>\n\t<head>\n\t\t<title></title>\n\t\
        <link rel = "stylesheet" href = "index.css">\n\t</head>\
            \n<body>\n\t{root.self_generate()}\n</body>\n</html>"""
            )







## development testing section

if __name__ == "__main__":
    from button import Button
    from input import Input
    from boxlayout import BoxLayout

    root = BoxLayout()
    layout = BoxLayout(xAlign = "flex-start",bgColor = "red")
    layout2 = BoxLayout(alignBy = "column",bgColor = "green")
    inp = Input( bgColor = "orange" ,mode = "password")
    btn = Button()
    layout.addComponent([inp,btn])
    layout2.addComponent([inp,btn])
    root.addComponent([layout,layout2])

    html = Html(root)


    with open("file.html","w") as htmlfile:
        
        htmlfile.write(html.template)

    with open("index.css","w") as cssfile:

        cssfile.write(root.style_generate())

##    print(layout.self_generate())
##    print(layout.style_generate())
