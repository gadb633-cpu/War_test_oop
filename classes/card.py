
class Card:
    def __init__(self,value,kind_card):
        self.value = value
        self.kind_card= kind_card

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,new_value):
        if self.value < 2 or self.value > 14:
            raise ValueError("out of range!!")
        if not isinstance(self.value,int):
            raise ValueError("enter only num!!")
        self._value = new_value

    @property
    def kind_card(self):
        return self._kind_card

    @kind_card.setter
    def kind_card(self,new_kind_card):
        if self.kind_card.lower() not in ["h","d","c","s"]:
            raise ValueError("the kind it's noy correct!")
        self._kind_card = new_kind_card

    def to_dict(self):
        return self.__dict__ 
    
    @classmethod
    def from_dict(cls,data):
        return 

