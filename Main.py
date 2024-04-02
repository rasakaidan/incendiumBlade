from stackStack import Stack
from playerClass import Player

if __name__ == "__main__":
    
    player1 = Player("Incendium")
    player2 = Player("Blade")
    card_stack = Stack()

    # hand class? tied to player? 
    player1.add_card_to_hand("Blast")
    player1.add_card_to_hand("Blast")
    player1.add_card_to_hand("Reflux")
    player1.add_card_to_hand("Storm")
    player1.add_card_to_hand("Pyro")
    player1.add_card_to_hand("Cocoon")
    player1.add_card_to_hand("Metamorphose")

    player2.add_card_to_hand("Blast")
    player2.add_card_to_hand("Blast")
    player2.add_card_to_hand("Reflux")
    player2.add_card_to_hand("Storm")
    player2.add_card_to_hand("Pyro")
    player2.add_card_to_hand("Cocoon")
    player2.add_card_to_hand("Metamorphose")

    print("Your Hand:", player1.hand)


    # this should be a function 
    #loop 
    players = [player1, player2]
    current_player_index = 0
    turns = 0
    while turns < 6:  # stack fills to 6 before executing
        current_player = players[current_player_index]

        # Player takes a turn
        if current_player.use_card(card_stack):
            print(f"{current_player.name} played.")
            turns += 1
        else:
            print(f"{current_player.name} couldn't play a card.")

        # Switch to the next player
        current_player_index = (current_player_index + 1) % 2

    # Execute cards in the stack from right to left
    print("Cards executed from right to left:")
    while not card_stack.is_empty():
        card = card_stack.pop()
        print(card)





