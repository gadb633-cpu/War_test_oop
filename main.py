from classes.card import Card
from classes.game_manager import Game
from inputs.inputs import Inputs
from menus.shaw_menu import Menu
from result.shaw_result import Shaw_result

def main():
    game = Game()
    game.make_deck()
    game.mixing()
    game.distribution_to_players()
    status = True
    while status:
        Menu.shew_menu()
        choice_out = Inputs.get_num("enter your choice [1,2]")
        match choice_out:
            case 1:
                round_game = game.make_round()
                msg = game.check_win_round(round_game[0],round_game[1])
                Shaw_result.shaw_round_result(round_game[0],round_game[1],msg,len(game.player.player_cards),len(game.computer.player_cards))
            case 2:
                Menu.shaw_menu_exit()
                choice_in = Inputs.get_num("enter your choice [1,2]")
                match choice_in:
                    case 1:
                        status= False
                        main()
                    case 2:
                        status = False
            case _:
                print("only 1 or 2!!!!!!")
main()
