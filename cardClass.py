class Card:

  def __init__(self, name, owner=None):
    self.name = name
    self.owner = owner

  def set_owner(self, player):
    self.owner = player

  def get_owner(self):
    return self.owner

  def play(self, player, targets):
    pass


class Blast(Card):

  def __init__(self):
    super().__init__("Blast")

  def play(self, player, opponents):
    for opponent in opponents:
      player.deal_damage(2, opponent)


class Reflux(Card):

  def __init__(self):
    super().__init__("Reflux")

  def play(self, player, targets):
    for target in targets:
      player.deal_damage(1, target)


class Storm(Card):

  def __init__(self):
    super().__init__("Storm")

  def play(self, player, targets):
    for target in targets:
      player.deal_damage(1, target)
      player.deal_damage(1, target)
      player.deal_damage(1, target)


class Cock(Card):

  def __init__(self):
    super().__init__("Coccoon")

  def play(self, player, targets):
    player.toggle_immunity()


class Meta(Card):

  def __init__(self):
    super().__init__("Metamorphose")

  def play(self, player, targets):
    player.toggle_meta()


class Pyro(Card):

  def __init__(self):
    super().__init__("Pyro")

  def play(self, player, targets):
    for target in targets:
      player.deal_damage(4, target)
