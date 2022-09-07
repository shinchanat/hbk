class Image: 
    
    count=0

    def __init__(self ,source, name ="image",padding = ['0px']*4,pos=["none",]*2,posMode = "relative",radius=["0px"]*4,
                 margin = ['10px']*4, size = ["100%"]*2):
        
            self.name = name+'-'+str(Image.count) if name =='image' else name
            self.source = source
            self.padding = padding
            self.pos = pos
            self.posMode = posMode
            self.radius = radius
            self.margin = margin
            self.size = size

    def style_generate(self):
        
        return  (f"\n.{self.name}"+'{\n\t'
                f"padding : {' '.join(self.padding)};\n\t"
                f"position : {self.posMode};\n\t"
                f"left : {self.pos[0]};\n\t"
                f"top : {self.pos[-1]};\n\t"
                f"border-radius : {' '.join(self.radius)};\n\t"
                f"margin : {' '.join(self.margin)};\n\t"
                f"width : {self.size[0]};\n\t"
                f"height : {self.size[-1]};\n" '}\n') 

    def self_generate(self):
        return f"\n<img class = '{self.name}' src = '{self.source}' alt = 'ImageNotFoundError'/>"
    

if __name__=="__main__":
        
    image=Image(source=r"C:\Users\Harish\Desktop\projects\1.png")
        
    print(image.self_generate())
        
    print(image.style_generate())
