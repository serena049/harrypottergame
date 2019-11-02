"""
The game: Harry rescues Ginny
Ginny was captured by Lord Voldemort, Harry gets a map from Hagrid and he needs
to go through a series halls/rooms at Hogwarts, each hall/room has a challenge
that he needs to take before going to the next. You are playing Harry, try your
best to save Ginny!
"""

"""
Scenes:
1. Death
2. Great Hall: beginning of the game. There are 100 Flobberworms (A 10 inch toothless brown worm).
You have to pick their favorite food to defeat them
3. The Astronomy Tower: You have to fight with a dragon, if you succeed, the dragon will take you to the
dark forest
4. Dark forest: This is where Ginny is captured. Here you need to guess which room Ginny is in
5. Gryffindor's common room: if you succeed, you will celebrate with you friends at teh common room
"""


"""
Map
- next_scene
- open_scene

Scene
- enter
    * Great hall
    * Astronomy Tower
    * Dark forest
    * Gryfiindor's common room
    * Death

Engine
- play
"""


class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class GreatHall(Scene):

    def enter(self):
        pass

class AstronomyTower(Scene):

    def enter(self):
        pass

class DarkForest(Scene):

    def enter(self):
        pass

class GryfiindorsCommonRoom(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('Hogwarts')
a_game = Engine(a_map)
a_game.play()
