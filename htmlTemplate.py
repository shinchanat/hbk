
class Html:
    def __init__(self,components = "helloworld"):
        self.template = (
            f"""<html>\n\t<head>\n\t\t<title>\n\t\t</title>\n\t\
            <link rel = "stylesheet" href = "index.css">\n\t</head>\
            \n<body>\n\t{components}\n</body>\n</html>""")







## development testing section

if __name__ == "__main__":
    from button import Button
    from input import Input

    field = Input(radius = (20,)*4,bgcolor = "skyblue",color = "black",pos = ("200px","200px"),
                  placeholder = "Enter your name : ",
                  padding = (30,)*4)
    
    html = Html(field.self_generate())
    css = field.style_generate()
    print(css)

    with open("file.html","w") as htmlfile:
        htmlfile.write(html.template)

    with open("index.css","w") as cssfile:
        cssfile.write(css)

    print(html.template)
