import random


class Deck(object):
  
  def __init__(self):
    self.deck = [] 
    contains = ["A", "K", "Q", "J", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.deck = [card for x in range(4) for card in contains]

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self, n):
    return [self.deck.pop() for _ in range(n)]
