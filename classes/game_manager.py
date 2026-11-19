from classes.card import Card
import random
from classes.player import Player

class Game:
    def __init__(self):
        self.list_cards = []
        self.player = Player("player")
        self.computer= Player("computer")

    def make_deck(self):
        count = 2
        kinds = ["♥","♦","♣","♠"]
        the_kind = 0
        for num in range(52):
            self.list_cards.append(Card(count,kinds[the_kind]))
            if count == 14:
                count = 2
                the_kind +=1
                continue
            count +=1

    def shuffle(self):
        for num in range(1000):
            num1 = random.randint(0,51)
            num2 = random.randint(0,51)
            if num1 == num2:
                num2 = random.randint(0,51)
            index_card = self.list_cards[num1]
            self.list_cards[num1] = self.list_cards[num2]
            self.list_cards[num2] = index_card

    def distribution_to_players(self):
        count = 0
        for num in range(26):
            self.player.add_card(self.list_cards[count])
            count +=1
            self.computer.add_card(self.list_cards[count])
            count +=1

    def check_win_round(self,player_card,computer_card):
        if player_card.value > computer_card.value:
            self.player.player_cards.append(computer_card)
            self.player.player_cards.append(player_card)
            return "player_ win"
        if player_card.value < computer_card.value:
            self.computer.player_cards.append(player_card)
            self.computer.player_cards.append(computer_card)
            return "computer_win"
        else:
            self.computer.player_cards.append(computer_card)
            self.player.player_cards.append(player_card)
            return "it's a draw!!"

    def make_round(self):
        player_card = self.player.player_cards[0]
        computer_card = self.computer.player_cards[0]
        del self.player.player_cards[0]
        del self.computer.player_cards[0]
        return [player_card,computer_card]
        