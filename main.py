#Main
import random

class player :
  __init__ (self, name)  :
    self.name = name
    self.total_gem = 0
    self.temp_gem = 0
    self.in_game = False

class Card :
  __init__(self, danger, type_danger, treasure, nbr_gem, relic, val_relic):
    self.danger = danger
    self.type_danger = type_danger
    self.treasure = treasure
    self.nbr_gem = nbr_gem
    self.relic = relic
    self.val_relic = val_relic
    
def create_deck() :
  deck = []
  val_treasure = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
  val_relic = [5, 5, 5, 10, 10]
  for i in range (15) :
    deck.append(Card(False, 0, True, val_treasure[i], False, 0))
  for i in range (1, 6) :
    for j in range (3) :
      deck.append(Card(True, i, False, 0, False, 0))
  for i in range (5) :
    deck.append(Card(False, 0, False, 0, True, val_relic[i]
  deck.shuffle()
  return deck
