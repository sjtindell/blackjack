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
    h, s = self.total_value(cards) 
    if h > 21 and s > 21:
      print("bust!")
    elif h == 21 or s == 21:
      print("blackjack!")
    else:
      pass


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
      self.show_cards(cards)
      self.check_value(self.total_value(cards))
      return self.total_value(cards)
      

class Dealer(Base):
  
  def play(self, cards, deck):
    while self.total_value(cards)[1] <= 21:
      self.show_cards(cards)
      h, s = self.total_value(cards)
      if s >= 17:
        break
      else:
        cards.extend(deck.deal(1))
    self.show_cards(cards)
    self.check_value(self.total_value(cards))
    return self.total_value(cards)



