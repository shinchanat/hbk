
class Html:
    def __init__(self,components = "helloworld"):
        self.template = (
            f"""<html>\n\t<head>\n\t\t<title>\n\t\t</title>\n\t\
            <link rel = "stylesheet" href = "index.css">\n\t</head>\
            \n<body>\n\t{components}\n</body>\n</html>""")







## development testing section

if __name__ == "__main__":
    from Button import Button

    button = Button(bgcolor = "orange",text = "PRESS")
    html = Html(button.self_generate())
    css = button.style_generate()
    print(css)

    with open("file.html","w") as htmlfile:
        htmlfile.write(html.template)

    with open("index.css","w") as cssfile:
        cssfile.write(css)

    print(html.template)
