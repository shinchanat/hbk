
from boxlayout  import BoxLayout

class Card:

    count = 0

    def __init__(self,name = "card",component = [],bgColor = "white",elevation = "10px"):
        self.name = name+'-'+str(Card.count) if name == "card" else name
        Card.count += 1
        self.component = component
        self.elevation = elevation
        self.card = BoxLayout(alignBy = "column",bgColor = bgColor)


    def style_generate(self):

        return self.card.style_generate()

    def self_generate(self):

        self.card.addComponent(self.component)

        return self.card.self_generate()



if __name__ == "__main__":

    from label import Label
    from button import Button

    l = Label()
    l1 = Label(text = "harish")
    btn = Button(text = "TestingButton")
    card = Card(component = [l,l1,btn])
    print(card.style_generate())
    print(card.self_generate())
