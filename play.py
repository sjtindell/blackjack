from deck import Deck
from game import Player, Dealer


d = Deck()
player = Player(100)
dealer = Dealer()

while True:
  bet = player.bet()
  dcards = d.deal(2)
  pcards = d.deal(2)
  pc_value = player.play(pcards, dcards[1], d)
  dc_value = dealer.play(dcards, d)
  
  if pc_value > 0 and dc_value > 0:
    if pc_value < dc_value:
      print("dealer wins")
    elif pc_value > dc_value:
      print("player wins")
      if pc_value == 21:
        player.win(bet * 1.5)
      else:
        player.win(bet * 2)    
  elif pc_value == -1 and dc_value > 0:
    print("dealer wins")
  elif dc_value == -1 and pc_value > 0:
    print("player wins")
    if pc_value == 21:
      player.win(bet * 2.5)
    else:
      player.win(bet * 2)
  
  print("bankroll: ", player.bankroll)
