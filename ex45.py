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
        final_scene = self.scene_map.go_to_scene('gryfiindorscommonroom')

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
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class GreatHall(Scene):

    def enter(self):
        print "You are Harry Potter and your friend Ginny was taken by Lord Voldemort!"
        print "Hagrid gave you a map, you need to go through a series halls/rooms at Hogwarts,"
        print "each hall/room has a challenge that you need to take before going to the next."
        print "Try your best to save Ginny! Good luck!\n"

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
        print "You are now at the Astronomy Tower and there is a giant black dragon waiting for you."
        print "What would you do? \n"
        print "A. You fight hard, with the new spell you've learned from class. \n"
        print "B. You tell a joke. Remember? You can talk to snakes, maybe the dragon can understand you as well. \n"
        print "C. You pet the dragon's head. He looks so cute. \n"
        print "D. You give the dragon the gummy bear you stealed from the flobberworms. \n"
        print "Now pick your choice!\n"

        action = raw_input()
        if action == 'A':
            print "Okay, you apprently didn't pay attention in the class. You used the wrong spell and turned yourself"
            print "into a little lamb. The dragon eat you and find you very yummy! You are dead."
            return 'death'

        if action == "B":
            print "Viola! It worked! Turns out that you are really gifted in talking to animals. The dragon finds your"
            print "joke very funny and he's very happy. He fly you to the dark forest."
            return "darkforest"

        if action == "C":
            print "Okay, the dragon is not a puppy/kitten. And you missed the head and touched his teeth..."
            print "The dragon tear you up and you are dead."
            return 'death'

        if action == "D":
            print "Common, this is so common sense - a dragon eats meat, and that's you. You are dead."
            return 'death'

        else:
            print "Not recognizing the input. Just choose among ABCD."
            return 'astronomytower'


class DarkForest(Scene):

    def enter(self):
        print "Now you are at the final place - the dark forest. The wind is blowing hard and you can barely see what's in fromt of you."
        print "There are 3 doors. One of them is locking up Ginny. Open the correct one and you will save her! Now pick your number!"

        action = int(raw_input("> "))
        answer = 3
        if action == answer:
            print "Congratulations! You have saved Ginny!!"
            return "gryfiindorscommonroom"
        elif action != answer:
            print "Bad luck! Lord Voldemort come out and beat you to death."
            return 'death'
        else:
            print "Not recognizing the input. Are you putting in a number?"
            return 'darkforest'

class GryfiindorsCommonRoom(Scene):

    def enter(self):
        print "Wow! You have successfully saved Ginny and all your professors and friends are so proud"
        print "of you! They are hosting a great party for you the Gryfiindor's Common Room, enjoy it, you've earned it!"
        return 'Finished! Congratulations!'

class Map(object):

    scenes = {
        'death': Death(),
        'greathall': GreatHall(),
        'astronomytower': AstronomyTower(),
        'darkforest': DarkForest(),
        'gryfiindorscommonroom': GryfiindorsCommonRoom(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def go_to_scene(self, scene_name):
        scene_class = Map.scenes.get(scene_name)
        return scene_class

    def go_to_the_first_scene(self):
        return self.go_to_scene(self.start_scene)


a_map = Map('greathall')
a_game = Engine(a_map)
a_game.play()
