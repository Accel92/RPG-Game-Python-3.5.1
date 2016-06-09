from .game.map1 import Map
from .game.core import Engine
 
beginning = Map()
engine1 = Engine(beginning)
engine1.play()
'''  alternative for testing (see also game/core/engine and game/map1/map)
a_map = Map("welcome")
a_game = Engine(a_map)
a_game.play()'''  
