
class Player:
    def __init__(self,name):
        self.name = name
        self.player_cards =[]

    def add_card(self,card):
        self.player_cards.append(card)
    