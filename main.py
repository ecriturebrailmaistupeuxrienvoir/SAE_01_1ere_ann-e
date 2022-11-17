#Main

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
