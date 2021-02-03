#Kassi Kassino players
#Kassi Kassino Version 1
from deck_module import deck
from hand_module import hand
from computer_move_func import player_turn
import func


#name = input("Please enter a name for player 1: ")
player_1 = hand("Edward")
player_2 = hand("Nelson")
player_3 = hand("Daniel")
player_4 = hand("Lewis")
table = hand()

player1_deck = hand()
player2_deck = hand()
player3_deck = hand()
player4_deck = hand()

player1_build = hand()
player2_build = hand()
player3_build = hand()
player4_build = hand()

players = [player_1, player_2, player_3, player_4]

deck = deck()
deck.populate()
deck.shuffle()
print("Cards in the deck: \n", deck, "\n")
deck.deal(players)

func.most_card(player_1)

while not player_1.is_empty():
    func.player_turn(player_1, player1_deck, player1_build, player3_deck, player4_deck, table, player3_build, player4_build, player_3, player_4)
    player_turn(player_2, player2_deck, player2_build, player3_deck, player4_deck, table, player3_build, player4_build, player_3, player_4)
    player_turn(player_3, player3_deck, player3_build, player1_deck, player2_deck, table, player1_build, player2_build, player_1, player_2)
    player_turn(player_4, player4_deck, player4_build, player1_deck, player2_deck, table, player1_build, player2_build, player_1, player_2)

input("Press enter to exit:")
