from stackClass import Stack
import cardClass
import playerClass


class Game:

    def __init__(self, stack, player1, player2):
        player1 = playerClass.Player("incendium")
        player2 = playerClass.Player("Blade")
        self.players = [player1, player2]
        self.stack = Stack

    def populate_hands(self):
        # Populating player 1's hand
        blast_card = cardClass.Blast()
        reflux_card = cardClass.Reflux()
        storm_card = cardClass.Storm()
        cock_card = cardClass.Cock()
        meta_card = cardClass.Meta()
        pyro_card = cardClass.Pyro()

        self.players[0].add_to_hand(blast_card)
        self.players[0].add_to_hand(reflux_card)
        self.players[0].add_to_hand(storm_card)
        self.players[0].add_to_hand(cock_card)
        self.players[0].add_to_hand(meta_card)
        self.players[0].add_to_hand(pyro_card)

        # Populating player 2's hand
        blast_card2 = cardClass.Blast()
        reflux_card2 = cardClass.Reflux()
        storm_card2 = cardClass.Storm()
        cock_card2 = cardClass.Cock()
        meta_card2 = cardClass.Meta()
        pyro_card2 = cardClass.Pyro()

        self.players[1].add_to_hand(blast_card2)
        self.players[1].add_to_hand(reflux_card2)
        self.players[1].add_to_hand(storm_card2)
        self.players[1].add_to_hand(cock_card2)
        self.players[1].add_to_hand(meta_card2)
        self.players[1].add_to_hand(pyro_card2)

    def round1(self, stack):
        stack.push(self.players[1].select_card())

        stack.push(self.players[0].select_card())
        stack.push(self.players[0].select_card())

        stack.push(self.players[1].select_card())
        stack.push(self.players[1].select_card())

        stack.push(self.players[0].select_card())

    def round2(self, stack):
        stack.push(self.players[0].select_card())

        stack.push(self.players[1].select_card())
        stack.push(self.players[1].select_card())

        stack.push(self.players[0].select_card())
        stack.push(self.players[0].select_card())

        stack.push(self.players[1].select_card())

    def flush(self, stack):
        played_cards = []

        for _ in range(len(self.players)):
            played_cards.append(stack.pop())

        for j in (played_cards):
            print(j.name)

        for i, card in enumerate(played_cards):
            targets = [
                player for idx, player in enumerate(self.players) if idx != i
            ]  # Assign targets for each card

            card.play(self.players[i],targets)  # Dynamic play action with flexible targets

            print(f"After playing {card.name}:")
            for player in self.players:
                print(f"{player.name}'s HP: {player.hp}")

            if self.players[0].hp <= 0:
                print(f"{self.players[1].name} wins the game!")
                break
            elif self.players[1].hp <= 0:
                print(f"{self.players[0].name} wins the game!")
                break
            else:
                print("No winner yet. Continue playing.")

