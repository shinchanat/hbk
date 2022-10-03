import webbrowser

class Html:
    
    def __init__(self,filename,root = None):
        self.root = root
        self.filename = filename
        self.template = (
            f"""<!DOCTYPE html5>\n<html lang = 'en'>\n\t<head>\n\t\t<title></title>\n\t\
        <link rel = "stylesheet" href = "{self.filename.replace('html','css')}">\n\t</head>"""+self.root.self_generate())

    def save(self):
        with open(f'{self.filename}','w') as htmlfile:
            htmlfile.write(self.template)

        with open(f'{self.filename.replace(".html",".css")}','w') as cssfile:
            cssfile.write(self.root.style_generate())

        webbrowser.open(f'{self.filename}')


## development testing section

if __name__ == "__main__":

    from boxlayout1 import BoxLayout
    from screen import Screen
    from button import Button
    from input import Input
    from label import Label
    from htmltemplate import Html

    testingpage = Screen()
    testingpage.addComponent([
        BoxLayout([
            Label("Username :"),
            Input(),
            Button()]),
        Button("Click")
        ])

    Html('testing.html',testingpage).save()
