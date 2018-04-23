import random
import time

class Coin:
  sides = ['heads', 'tails']
  
  def __init__(self, name):
    self.name = name
    
  def flip(self):
    side = random.choice(Coin.sides)
    return side
  
  def displayInfo(self):
    print("{} flipped {}".format(self.name, self.flip()))
    
dime = Coin('dime')
penny = Coin('penny')
quarter = Coin('quarter')
nickel = Coin('nickel')

for x in range(10):
  dime.displayInfo()
  penny.displayInfo()
  quarter.displayInfo()
  nickel.displayInfo()
  print("\n")
  time.sleep(2)