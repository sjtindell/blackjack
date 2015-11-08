import random


class Deck(object):
  
  def __init__(self):
    self.deck = []
    self.replenish()
    self.shuffle()
  
  def __repr__(self):
    return " ".join(str(i) for i in self.deck)

  def replenish(self):
    contains = ["A", "K", "Q", "J", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.deck = [card for x in range(4) for card in contains]
    self.shuffle()
    

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self, n):
    try:
      cards = [self.deck.pop() for _ in range(n)]
    except IndexError:
      print("deck exhausted")
      print("deck: ", self.deck)
      self.replenish()
      cards = [self.deck.pop() for _ in range(n)]
    return cards
      

