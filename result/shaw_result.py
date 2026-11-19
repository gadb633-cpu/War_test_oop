
class Shaw_result:
    staticmethod
    def shaw_round_result(player_card,computer_card,winner_msg,num_card_player,num_card_computer):
        print(f'''
        ============== TURN ===============
        player_card: {player_card.get_type_num()} {player_card.kind_card}
        computer_card: {computer_card.get_type_num()} {computer_card.kind_card}
        {winner_msg}
        num_card_player: {num_card_player} | num_card_computer: {num_card_computer}
        ===================================
        ''')