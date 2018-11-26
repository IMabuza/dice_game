#class definition for an n-sided die

#import packages

import random

class MSdie:

  #Current die value

  current_value = None

  #constructor here

  def __init__(self,numOfSides):
    self.numOfSides = numOfSides

  #define classmethod 'roll' to roll the MSdie
  # 
  def roll(self):

    if self.current_value != None:
      return self.current_value
    else:
      self.current_value = random.randint(1, self.numOfSides)
      return self.current_value
    

  #define classmethod 'getValue' to return the current value of the MSdie

  def getValue(self):

    return self.current_value

  #define classmethod 'setValue' to set the die to a particular value

  def setValue(self, value):
    self.current_value = value

#Create Die Object with number of sides
die = MSdie(13)
#set die value (cheat)
die.setValue(3)
#print the value
print(die.getValue())
#roll die 
print(die.roll())