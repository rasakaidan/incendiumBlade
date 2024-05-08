class Player:

  def __init__(self, name, hp=15, immunity=False, meta=False):
    self.name = name
    self.hp = hp
    self.immunity = immunity
    self.meta = meta
    self.hand = []

  def take_damage(self, amount):
    if not self.immunity:
      self.hp -= amount

  def deal_damage(self, amount, opponent):
    if self.meta:
      opponent.take_damage(amount + 2)
    else:
      opponent.take_damage(amount)

  def toggle_immunity(self):
    self.immunity = not self.immunity

  def toggle_meta(self):
    self.meta = not self.meta

  def add_to_hand(self, card):
    self.hand.append(card)
    card.set_owner(self)

  def select_card(self):
    for i, card in enumerate(self.hand):
      print(f"{i+1}. {card.name}")
    choice = input("Enter the number of the card you want to play:")
    try:
      choice_index = int(choice) - 1
      if 0 <= choice_index < len(self.hand):
        card = self.hand.pop(choice_index)
        print(f"{self.name} played {card.name}")
        return card
      else:
        print("Invalid choice. Please enter a number within the range.")
    except ValueError:
      print("Invalid input. Please enter a number.")

    return False
