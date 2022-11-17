#Main

class player :
  __init__ (self, name)  :
    self.name = name
    self.total_gem = 0
    self.temp_gem = 0
    self.in_game = False
    
  def add_temp_gem(self, gem) :
    self.temp_gem += gem
   
  def delete_temp_gem(self) :
    self.temp_gem = 0
    
  def enter_game(self) :
    self.in_game = True
  
  def quit_game(self) :
    self.in_game = False
    
  def add_total_gem(self, value) :
    self.total_gem += value
  
  def get_temp_gem(self):
    return self.temp_gem
  
  def get_total_gem(self):
    return self.total_gem
  
