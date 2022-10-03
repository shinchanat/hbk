from css_statements import *

def generate(default_design,component):


        css = f".{component.name}""{\n\t"
    
        for propTyp , propVal in component.props.items():
            
            """
                Generates a css code for the component , this runs if parameter
                is passed by the user.
            """
            
            if propTyp not in props_name : # Checks wether the property is defined in 'css_statement.py, 'props_name' is defined in css_statements.py'.
                print("invalid argument.")
                break
            default_design.update({ propTyp :css_statements[propTyp]+str(propVal)+";\n\t"}) # Generates a css { property : value } statement.

        
        for propTyp , propVal in default_design.items():
            
            css += str(default_design[propTyp])
                
        css += "}"
        
        return css
