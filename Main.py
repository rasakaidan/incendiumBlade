import gameClass
import playerClass

if __name__ == "__main__":
  stack = gameClass.Stack()
  player1 = playerClass.Player("Player 1")
  player2 = playerClass.Player("Player 2")

  game = gameClass.Game(stack, player1, player2)
  game.populate_hands()
  print(game.players[1].hand)

  game.round1(stack)
  game.flush(stack)
  game.round2(stack)
  game.flush(stack)
