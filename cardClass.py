class Card:
    def __init__(self, name):
        self.name = name

    # does this need two inputs? target player and source player?
    # where do i track this? 
    def execute_action(self, player):
        if self.name == "Blast":
            player.take_damage(2)
            print(f"{player.name} takes 2 damage from Blast.")

        # Pyro card 
        elif self.name == "Pyro":
            player.take_damage(4)
            print(f"{player.name} takes 4 damage from Pyro!")

        elif self.name == "Storm":
            player.take_damage(1)
            player.take_damage(1)
            player.take_damage(1)
            print(f"{player.name} is buffeted by a Storm!")

        # this needs a counter
        #elif self.name == "Reflux":
        #    player.something blah blah
        
        # also needs a counter
        #elif self.name == "Coccon":
        #    player.whatever

        # counterino
        #elif self.name == "Metamorphosis":
        #    player.something 
