class Player:
    def __init__(self, name, hp=15, immunity=False):
        self.name = name
        self.hp = hp
        self.immunity = immunity
        self.hand = []  # Initialize an empty hand
        self.used_cards = set()  # Initialize an empty set for used cards

    def take_damage(self, damage):
        if not self.immunity:
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0

    # could do heal as negative damage?
 
    # need 3 counters - should be tied to player (reflux and metamorph AND cocoon)

    def toggle_immunity(self):
        self.immunity = not self.immunity

    def is_alive(self):
        return self.hp > 0

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def use_card(self, stack):
        for i, card in enumerate(self.hand):
            print(f"{i+1}. {card}")
        choice = input("Enter the number of the card you want to play: ")
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.hand):
                card = self.hand.pop(choice_index)
                if card not in self.used_cards:
                    self.used_cards.add(card)
                    stack.push(card)  # Push the used card onto the stack
                    return True
                else:
                    print("This card has already been used.")
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        return False

    def print_available_cards(self):
        print(f"{self.name}'s Hand - Available Cards:")
        for card in self.hand:
            print(card)