from css_statements import *
import element_style_generator


default_design = {
    "sizeX" : "width : 50px;\n\t",
    "radius" : "border-radius : 0px;\n\t",
    }

class Image: 
    
    count = 0

    def __init__(self ,source, name ="image",**props):
        
            self.name = name+'-'+str(Image.count) if name =='image' else name
            self.source = source
            self.props = props
            self.default_design = default_design
            Image.count += 1

    def style_generate(self):

        return element_style_generator.generate(default_design,self)

    def self_generate(self):
        return f"\n<div style = '{default_design['radius']}'><img class = '{self.name}' src = '{self.source}' alt = 'ImageNotFoundError'/></div>"
    

if __name__=="__main__":
        
    image=Image(source=r"C:\Users\Harish\Desktop\projects\src\1.png")
        
    print(image.self_generate())
        
    print(image.style_generate())
