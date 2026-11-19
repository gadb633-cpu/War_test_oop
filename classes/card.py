
class Card:
    def __init__(self,value,kind_card):
        self.value = value
        self.kind_card= kind_card
        self.dict_type_cards = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:"J",12:"Q",13:"K",14:"A"}

    def get_card(self):
        return self.dict_type_cards[self.value],self.kind_card
    
    def get_type_num(self):
        return self.dict_type_cards[self.value]