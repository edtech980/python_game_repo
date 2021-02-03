#Kassi Kassino functions
#Kassi Kassino Version 1

def option(player):
    options = ("""
                1) Throw down card
                2) Build a card
                3) Devour cards
                """)
    print(options)
    print(player.name, "please pick a choice:")
    option = input("Choice: ")
    return option

def throw_down(player, card, table):
    player.give(player.cards[card], table)

def most_card(player):
    most_cards = player.card_num()
    print(most_cards.most_common())
    
    print(most_cards[1])
    

def card_devour(player, card, player_build, player_deck):
    while not player_build.is_empty():
        player_build.give(player_build.cards[0], player_deck)
    player.give(player.cards[card], player_deck)

def devour(player, card, player_build, player_deck, player1_build, player2_build, player1, player2, table):
    print("Before devouring cards:")
    print(player.name, "Cards:\t", player)
    print(player.name, "Deck:\t", player_deck)
    print(player.name, "Build:\t", player_build, "\n")
    print(player1.name, "Build:\t", player1_build)
    print(player2.name, "Build:\t", player2_build)
    print("Table Cards:\t", table, "\n")

    print("Please choose the cards you want to devour:")
    print("\t\t1) Your Build")
    print("\t\t2)", player1.name, "Build")
    print("\t\t3)", player2.name, "Build")
    print("\t\t4) Table Cards\n")

    print(player.name, "please pick a choice:")
    

    choice = input()
    print()
    if choice == "1" and not player_build.is_empty():
        while not player_build.is_empty():
            player_build.give(player_build.cards[0], player_deck)
        player.give(player.cards[card], player_deck)
    elif choice == "2" and not player1_build.is_empty():
        while not player1_build.is_empty():
            player1_build.give(player1_build.cards[0], player_deck)
        player.give(player.cards[card], player_deck)
    elif choice == "3" and not player2_build.is_empty():
        while not player2_build.is_empty():
            player2_build.give(player2_build.cards[0], player_deck)
        player.give(player.cards[card], player_deck)
    elif choice == "4" and not table.is_empty():
        while not table.is_empty():
            table.give(table.cards[0], player_deck)
        player.give(player.cards[card], player_deck)
    else:
        player.give(player.cards[card], table)
    print("\nAfter devouring cards:")
    print(player.name, "Cards:\t", player)
    print(player.name, "Deck:\t", player_deck)
    print(player.name, "Build:\t", player_build, "\n")
    print(player1.name, "Build:\t", player1_build)
    print(player2.name, "Build:\t", player2_build)
    print("Table Cards:\t", table, "\n")


    
def player_turn(player, player_deck, player_build, player2_deck, player3_deck, table, player2_build, player3_build, player1, player2):
    print(player.name, "Cards:\t", player)
    print(player.name, "Build:\t", player_build)
    print(player.name, "Deck:\t", player_deck)
    print("Table Cards:\t", table, "\n")
    opt = option(player)
    print()
    if opt == "1":
        throw_down(player, 0, table)
    elif opt == "2":
        build(player, 0, player_build, player2_deck, player3_deck, table, player1, player2)
    elif opt == "3":
        devour(player, 0, player_build, player_deck, player2_build, player3_build, player1, player2, table)
    else:
        throw_down(player, 0, table)
    print(player.name, "Cards:\t", player)
    print(player.name, "Build:\t", player_build)
    print(player.name, "Deck:\t", player_deck)
    print("Table Cards:\t", table, "\n")

def build(player_1, card, player1_build, player2_deck, player3_deck, table, player2, player3):
    choice = None
   
    while choice != "0":
        print("\n", player_1.name, "Cards:\t", player_1)
        print(player_1.name, "Build:\t", player1_build)
        print(player2.name, "Deck:\t", player2_deck)
        print(player3.name, "Deck:\t", player3_deck)
        print("Table Cards:\t", table, "\n")
        print(player_1.name, "pick from the deck you want to take a card from:")
        print("\t\t0) Exit build")
        print("\t\t1) From", player2.name, "Deck")
        print("\t\t2) From", player3.name, "Deck")
        print("\t\t3) From Table\n")

        choice = input("Pick your choice: ")
        print()
        if choice == "1":
            if not player2_deck.is_empty():
                player2_deck.give(player2_deck.cards[card], player1_build)
            else:
                print(player2.name, "Deck is empty.")
        elif choice == "2":
            if not player3_deck.is_empty():
                player3_deck.give(player3_deck.cards[card], player1_build)
            else:
                print(player3.name, "Deck is empty.")
        elif choice == "3":
            if not table.is_empty():
                table.give(table.cards[card], player1_build)
            else:
                print("Table is empty:\n")
    player_1.give(player_1.cards[card], player1_build)
    print()
    print("Cards after exiting build: ")
    
