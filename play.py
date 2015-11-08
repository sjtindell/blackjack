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
  #print(d.deck)
