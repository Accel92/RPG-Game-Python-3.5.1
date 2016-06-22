# Game engine info.


~This work has more functionality done than real plot to use it for, so it looks pretty raw. It is only that I have more heart for backend functionality than actual plot.


Game basis is a map module with locations dictionary. Engine is going through locations. Every location is a class with start method. Engine's purpose is to read every location method's return (it indicates the next location to be entered). 
Engine has an exception handling basis for going to final location. It is done so there could be multiple locations and endings. Also it is used for reusability for an engine for any new map to be done.

Player is generated when the game starts. Later on it is only expaned with features common for profession he takes, levels etc.
Every enemy (currently not many) is based on Enemy superclass which is extended.

Player's professions are done specifically the way to be easily added without much effort. It means that to have new profession it is only needed to create new module with profession class the way firts one's are done -> fighting method handles everything inside itself.

Fighting method takes enemy instance and runs the fight with player character. It calls for player's class attack method which handles player's skill choice according to skills he has due to his profession and level.



I have been thinking how to scale enemy to the player character. It is handled with special player template class. Every time enemy is instantiated it creates player template instance with the same level as enemy. It uses player template's statistics (they are the same as for player character class) and uses it as for it's statistics basis.

One may ask why I didn't use actual player class as I had one. Well, actually Player class stats are scaled with exp - not level so the easiest way was to create a small template class with only stats calculation bu based on actual level.
