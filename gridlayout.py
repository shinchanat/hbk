class GridLayout:

    count = 0
    
    def __init__(self,name = 'gridlayout',rows = 'none',cols = 'none',size = ('100%',)*2,bgColor = 'transparent',
                 padding = ['0px']*4,margin = ['0px']*4,space = {'column':'0px','row':'0px'}):

        if rows == 'none' and cols == 'none':
            raise Exception("'row' or 'column' must be defined.")

        self.name = name+'-'+str(GridLayout.count) if name == 'gridlayout' else name
        self.cols = cols
        self.rows = rows
        self.size = size
        self.margin = margin
        self.padding = padding
        self.space = space
        self.bgColor = bgColor
        GridLayout.count += 1
        self.__layout = ''
        self.__design = ''


    def style_generate(self):

        grid_template_mode = f'grid-template-columns : repeat({self.cols},1fr)' if self.rows == 'none' else f'grid-template-rows : repeat({self.rows},1fr)'

        self.__design +=(
            f'\n.{self.name}'+'{\n\t'
            'display : grid;\n\t'
            f'{grid_template_mode};\n\t'
            f'height : {self.size[-1]};\n\t'
            f'width : {self.size[0]};\n\t'
            f'background-color : {self.bgColor};\n\t'
            f'column-gap : {self.space.get("column","0px")};\n\t'
            f'row-gap : {self.space.get("row","0px")};\n\t'
            f'margin : {" ".join(self.margin)};\n\t'
            f'padding : {" ".join(self.padding)};\n'
            '}\n\n'
            )

        return self.__design
        
    def addComponent(self,component):

        if type(component).__name__ != 'list':
            
            raise Exception(f"{type(component).__name__} is not an iteratable.")

        for comp in component:

            self.__design += comp.style_generate()

        self.__layout = f"<div class = '{self.name}'>"+'\n'.join([comp.self_generate() for comp in component])+"\n</div>\n"

        return self.__layout

    def self_generate(self):

        return self.__layout
            

if __name__ == '__main__':

    from label import Label
    from input import Input

    gridlayout = GridLayout(rows = 2)
    gridlayout.addComponent([Label()])
    print(gridlayout.self_generate())
    print(gridlayout.style_generate())
