
class Card:
    def __init__(self,value,kind_card):
        self.value = value
        self.kind_card= kind_card

    def get_card(self):
        return self.value,self.kind_card
