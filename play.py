from deck import Deck
from game import Player, Dealer

d = Deck()
player = Player(100)
dealer = Dealer()
turn = 0

while True:
  d.shuffle()
  dcards = d.deal(2)
  pcards = d.deal(2)
  pc_value = player.play(pcards, dcards[1], d)
  print
  dc_value = dealer.play(dcards, d)
  print
  if pc_value > 0 and dc_value > 0:
    if pc_value < dc_value:
      print("dealer wins")
    else:
      print("player wins")
  elif pc_value == -1 and dc_value > 0:
    print("dealer wins")
  elif dc_value == -1 and pc_value > 0:
    print("player wins")

  #print(d.deck)
