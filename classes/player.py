
class Player:
    def __init__(self,name,list_cards):
        self.name = name
        self.list_cards =list_cards

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        if not self.name or self.name.strip() == "":
            raise ValueError("name not correct , try again!!")     
        self._name = new_name

    @property    
    def list_cards(self):
        return self._list_cards

    @list_cards.setter
    def list_cards(self,new_list_cards):
        if not isinstance(self.list_cards,list):
            raise ValueError("not correct,try again!!")
        self._list_cards = new_list_cards
    