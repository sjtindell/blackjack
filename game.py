class Base(object):  

  def total_value(self, cards):   
    hard, soft = 0, 0

    for card in cards:
      if card in ("K", "Q", "J"):
        hard += 10
        soft += 10
      elif type(card) is int:
        hard += card
        soft += card
      elif card == "A":
        hard += 11
        soft += 1

    return hard, soft

  def show_cards(self, cards): 
    card_string = " ".join(str(card) for card in cards)
    print(card_string)

  def check_value(self, cards):
    # -1 if bust, # if not, 1 if blackjack
    h, s = self.total_value(cards)
    if h > 21 and s > 21:
      print("bust!")
      return -1
    elif h == 21 or s == 21:
      print("blackjack!")
      return 1
    elif h > 21 and s < 21:
      print("stood on", s)
      return s
    elif h < 21:
      print("stood on", h)
      return h
    

class Player(Base):
  
  def __init__(self, bankroll):
    self.bankroll = bankroll

  def bet(self):
    bet = input("bet: $")
    self.bankroll -= bet
    return bet

  def win(self, amount):
    self.bankroll += amount
   
  def play(self, cards, dcard, deck):
    while self.total_value(cards)[1] < 21:
      print(dcard)
      self.show_cards(cards)
      play = input("> ")
      if play == "h":
        cards.extend(deck.deal(1))
      elif play == "s":
        break 
    value = self.check_value(cards)
    return value
      

class Dealer(Base):
  
  def play(self, cards, deck):
    self.show_cards(cards)
    while self.total_value(cards)[1] <= 21:
      h, s = self.total_value(cards)
      if s >= 17:
       break 
      else:
        cards.extend(deck.deal(1))
        self.show_cards(cards)
    value = self.check_value(cards)
    return value



