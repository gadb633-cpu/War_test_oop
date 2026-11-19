
class Shaw_result:
    staticmethod
    def shaw_round_result(player_card,computer_card,winner_msg,num_card_player,num_card_computer):
        print(f'''
        ============== TURN ===============
        player_card: {player_card.value} {player_card.kind_card}
        computer_card: {computer_card.value} {computer_card.kind_card}
        {winner_msg}
        num_card_player: {num_card_player} | num_card_computer: {num_card_computer}
        ===================================
        ''')