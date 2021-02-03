#Kassi Kassino functions
#Kassi Kassino Version 1
import random

def option(player, player2_deck, player3_deck, table, player1_build, player2_build, player3_build):
    print(player.name + "'s turn to play")
    print()
    options = ("""
                1) Throw down card
                2) Build a card
                3) Devour cards
                """)
    print(options)
    
    option = str(random.randrange(1, 4))
    if option == "1":
        return option
    elif option == "2":
        if not player2_deck.is_empty() or not player3_deck.is_empty() or not table.is_empty():
            return option
        else:
            option = random.choice(["1", "3"])
            if option == "3":
                if not player1_build.is_empty() or not player2_build.is_empty() or not player3_build.is_empty() or not table.is_empty():
                    return option
                else:
                    option = "1"
                    return option
    else:
        if not player1_build.is_empty() or not player2_build.is_empty() or not player3_build.is_empty() or not table.is_empty():
            return option
        else:
            option = "1"
            return option
    
    return option

def throw_down(player, card, table):
    player.give(player.cards[card], table)

def card_builder(num):
    pass

def card_devour(player, card, player_build, player_deck):
    while not player_build.is_empty():
        player_build.give(player_build.cards[0], player_deck)
    player.give(player.cards[card], player_deck)

def devour(player, card, player_build, player_deck, player1_build, player2_build, player1, player2, table):
    print("Before devouring cards:")
    print(player.name, "Cards:\t", player)
    print(player.name, "Deck:\t", player_deck)
    print(player.name, "Build:\t", player_build)
    print(player1.name, "Build:\t", player1_build)
    print(player2.name, "Build:\t", player2_build)
    print("Table Cards:\t", table)
    print()
    print(player.name, "will choose the cards he wants to devour:")
    print("\t\t1) Your Build")
    print("\t\t2)", player1.name, "Build")
    print("\t\t3)", player2.name, "Build")
    print("\t\t4) Table Cards")
    print()
    
    choices = ["1", "2", "3", "4"]
    choice = None
    devoured = False
    print()
    while devoured == False:
        choice = random.choice(choices)
        if choice == "1" and not player_build.is_empty():
            while not player_build.is_empty():
                player_build.give(player_build.cards[0], player_deck)
            player.give(player.cards[card], player_deck)
            print(player.name + " just devoured his own build")
            devoured = True
           
        elif choice == "2" and not player1_build.is_empty():
            while not player1_build.is_empty():
                player1_build.give(player1_build.cards[0], player_deck)
            player.give(player.cards[card], player_deck)
            print(player.name + " just devoured " + player1.name + "'s build")
            devoured = True
        elif choice == "3" and not player2_build.is_empty():
            while not player2_build.is_empty():
                player2_build.give(player2_build.cards[0], player_deck)
            player.give(player.cards[card], player_deck)
            print(player.name + " just devoured " + player2.name + "'s build")
            devoured = True
        elif choice == "4" and not table.is_empty():
            while not table.is_empty():
                table.give(table.cards[0], player_deck)
            player.give(player.cards[card], player_deck)
            print(player.name + " just devoured Table Cards")
            devoured = True
        else:
            if devoured == False:
                choices.pop(choices.index(choice))
    print("\nAfter devouring cards:")
    print(player.name, "Cards:\t", player)
    print(player.name, "Deck:\t", player_deck)
    print(player.name, "Build:\t", player_build)
    print(player1.name, "Build:\t", player1_build)
    print(player2.name, "Build:\t", player2_build)
    print("Table Cards:\t", table)
    print()


    
def player_turn(player, player_deck, player_build, player2_deck, player3_deck, table, player2_build, player3_build, player1, player2):
    print(player.name, "Cards:\t", player)
    print(player.name, "Build:\t", player_build)
    print(player.name, "Deck:\t", player_deck)
    print("Table Cards:\t", table)
    print()
    opt = option(player, player2_deck, player3_deck, table, player_build, player2_build, player3_build)
    print()
    
    if opt == "1":
        print(player.name, "chose to throw down a card")
        print()
        throw_down(player, 0, table)
    elif opt == "2":
        print(player.name, "chose to build a card")
        print()
        build(player, 0, player_build, player2_deck, player3_deck, table, player1, player2)
    elif opt == "3":
        print(player.name, "chose to devour cards")
        print()
        devour(player, 0, player_build, player_deck, player2_build, player3_build, player1, player2, table)
    else:
        print(player.name, "will throw down a card")
        print()
        throw_down(player, 0, table)
    print(player.name, "Cards:\t", player)
    print(player.name, "Build:\t", player_build)
    print(player.name, "Deck:\t", player_deck)
    print("Table Cards:\t", table)
    print()
    input("Press enter to continue:")
    print()

def build(player_1, card, player1_build, player2_deck, player3_deck, table, player2, player3):
    choices = ["0", "1", "2", "3"]
    choice = None
    while choice != "0":
        
        choice = random.choice(choices)
        
        print()
        if choice == "1" and not player2_deck.is_empty():
            print()
            print(player_1.name, "Cards:\t", player_1)
            print(player_1.name, "Build:\t", player1_build)
            print(player2.name, "Deck:\t", player2_deck)
            print(player3.name, "Deck:\t", player3_deck)
            print("Table Cards:\t", table, "\n")
            print(player_1.name, "is going to choose a deck he wants to take a card from:")
            print("\t\t0) Exit build")
            print("\t\t1) From", player2.name, "Deck")
            print("\t\t2) From", player3.name, "Deck")
            print("\t\t3) From Table")
            print()
            print(player_1.name + " took " + player2.name + "'s card")
            player2_deck.give(player2_deck.cards[card], player1_build)

        elif choice == "2" and not player3_deck.is_empty():
            print()
            print(player_1.name, "Cards:\t", player_1)
            print(player_1.name, "Build:\t", player1_build)
            print(player2.name, "Deck:\t", player2_deck)
            print(player3.name, "Deck:\t", player3_deck)
            print("Table Cards:\t", table, "\n")
            print(player_1.name, "is going to choose a deck he wants to take a card from:")
            print("\t\t0) Exit build")
            print("\t\t1) From", player2.name, "Deck")
            print("\t\t2) From", player3.name, "Deck")
            print("\t\t3) From Table")
            print()
            print(player_1.name + " took " + player3.name + "'s card")
            player3_deck.give(player3_deck.cards[card], player1_build)
 
        elif choice == "3" and not table.is_empty():
            print()
            print(player_1.name, "Cards:\t", player_1)
            print(player_1.name, "Build:\t", player1_build)
            print(player2.name, "Deck:\t", player2_deck)
            print(player3.name, "Deck:\t", player3_deck)
            print("Table Cards:\t", table, "\n")
            print(player_1.name, "is going to choose a deck he wants to take a card from:")
            print("\t\t0) Exit build")
            print("\t\t1) From", player2.name, "Deck")
            print("\t\t2) From", player3.name, "Deck")
            print("\t\t3) From Table")
            print()
            print(player_1.name, "took from Table Cards")
            table.give(table.cards[card], player1_build)
        elif choice == "0":
            print()
            print(player_1.name, "Cards:\t", player_1)
            print(player_1.name, "Build:\t", player1_build)
            print(player2.name, "Deck:\t", player2_deck)
            print(player3.name, "Deck:\t", player3_deck)
            print("Table Cards:\t", table, "\n")
            print(player_1.name, "is going to choose a deck he wants to take a card from:")
            print("\t\t0) Exit build")
            print("\t\t1) From", player2.name, "Deck")
            print("\t\t2) From", player3.name, "Deck")
            print("\t\t3) From Table")
            print()
            print(player_1.name, "chose to exit build")
    
        else:
            choices.pop(choices.index(choice))

    player_1.give(player_1.cards[card], player1_build)
    print()
    print("Cards after exiting build: ")
    
