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
        print Death.quips[randint(0, len(self.quips))]
        exit(1)

class GreatHall(Scene):

    def enter(self):
        print "You are Harry Potter and your friend Ginny was taken by Lord VoLord Voldemort!"
        print "Hagrid gave you a map, you need to go through a series halls/rooms at Hogwarts,"
        print "each hall/room has a challenge that you need to take before going to the next."
        print " Try your best to save Ginny! Good luck!\n"

        print "You are at the Great Hall. This is the beginning of the game."
        print "Suddenly, 100 Flobberworms (A 10 inch toothless brown worm) jump out!"
        print "Their general present you a bag of gummy bear, and you have to pick their favorite color! Type in the color!"

        action = raw_input("> ").lower()

        if action == 'red':
            print "Seriously? You really picked a color that reprent your blood?"
            print "Man, this is not a good sign. The Flobberworms get so angry and they fly into you and eat your head."
            print "You are dead."
            return 'death'

        if action == "yellow":
            print "Hmmm...The Flobberworms are yellow, so they feel very offended when you pick yellow. "
            print "They blast out their yello juicy to poison you and you are drowned to death."
            return 'death'

        if action == "green":
            print "Ah! Very close, the Flobberworms decide to give you another chance!"
            return 'greathall'

        if action == "blue":
            print "Yeah! You've picked the right color! The Flobberworms are very happy, they begin eatting all the blue gummy bears."
            print "And it gives you time to sneak away, and quietly go to the Astronomy tower."
            return 'astronomytower'

        else:
            print "Not recognizing the input! Remember, gummy bears only have 4 colors! Try again!"
            return "greathall"



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
