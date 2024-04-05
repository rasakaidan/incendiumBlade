class Card:
    def __init__(self, name):
        self.name = name

    def execute_action(self, player):
        if self.name == "Blast":
            player.take_damage(2)
            print(f"{player.name} takes 2 damage from Blast.")
        elif self.name == ""