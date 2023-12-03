from Settings import *
from runGame import runGame
from runRacing import runRacing

class Main():

    def __init__(self):

        # general
        self.game = runGame()
        

    def run(self):

        if self.game.state == False:
            self.game.run()
        
        if self.game.state:
            self.racing = runRacing(self.game.cars_name, self.game.map_number)
            self.racing.run()
        
Main().run()