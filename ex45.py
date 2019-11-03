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

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "entering base scene..."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.go_to_the_first_scene()
        final_scene = self.scene_map.go_to_scene('finished')

        while current_scene != final_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.go_to_scene(next_scene_name)

        # print out the final scene
        current_scene.enter()

class Death(Scene):

    quips = [
    "You died. You are definitely not a Harry Potter Fan!",
    "Shame on you! You failed to save your future wife!",
    "I bet Dobby can do a better job than you!",
    "This is not the right game for you, go back to Dota2!"
    ]

    def enter(self):
        print De

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

class Finished(Scene):

    def enter(self):
        pass

    def next_scene(self):
        pass

class Map(object):

    scenes = {
        'death': Death(),
        'greathall': GreatHall(),
        'astronomytower': AstronomyTower(),
        'darkforest': DarkForest(),
        'gryfiindorscommonroom': GryfiindorsCommonRoom(),
        'finished': Finished()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def go_to_scene(self, scene_name):
        scene_class = Map.scenes.get(scene_name)
        return scene_class

    def go_to_the_first_scene(self):
        return self.go_to_the_first_scene(self.start_scene)


a_map = Map('Hogwarts')
a_game = Engine(a_map)
a_game.play()
