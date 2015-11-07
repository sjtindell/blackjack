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


def total_value(cards):
  hard, soft = 0, 0
  for card in cards:
    if card in ("K", "Q", "J"):
      hard += 10
      soft += 10
    elif type(card) is int:
      hard += card
      soft += card
    else:
      hard += 11
      soft += 1
  return hard, soft


def check_value(value):
  h, s = value
  if h > 21 and s > 21:
    print("bust!")
  elif h == 21 or s == 21:
    print("blackjack!")
  else:
    pass

def player_round():
  print("player round")
  #bet = raw_input("bet: ")
  while total_value(player_cards)[1] < 21:
    card_string = " ".join(str(card) for card in player_cards)
    print(dealer_cards[1])
    print(card_string)
    play = raw_input("> ")
    if play == "h":
      player_cards.extend(d.deal(1))
    elif play =="s":
      break
  card_string = " ".join(str(card) for card in player_cards)
  print(card_string)
  check_value(total_value(player_cards))
  print("end player round")
  return total_value(player_cards)

def dealer_round():
  print("dealer_round")
  while total_value(dealer_cards)[0] <= 21:
    card_string = " ".join(str(card) for card in dealer_cards)
    print(card_string)
    s, h = total_value(dealer_cards)
    if s >= 17 or h >= 17:
      break
    else:
      dealer_cards.extend(d.deal(1))
  card_string = " ".join(str(card) for card in dealer_cards)
  print(card_string)
  check_value(total_value(dealer_cards))
  print("end dealer round")
  return total_value(dealer_cards)


d = Deck()

while True:
  bankroll = 100
  d.shuffle()
  dealer_cards = d.deal(2)
  player_cards = d.deal(2)
  pc_value = player_round()
  print
  dc_value = dealer_round()
  print(pc_value, dc_value)
  print
  #print(d.deck)
