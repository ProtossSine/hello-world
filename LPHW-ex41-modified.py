# -*- coding:utf-8 -*-
from sys import  exit
from random import  randint


class Scene(object):

    def __enter__(self):
        print("this scene is not yet configured. subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n--------")
            next_scene_name = current_scene.__enter__()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = [
        "u died.",
        "your mom will be proud ",
        "such a loser.",
        "I have a small puppy that's better at this"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def __enter__(self):
        print("balalalalla")

        action = raw_input(">>>>>>")

        if action == "shoot":
            print("sb\n")
            return "death"

        elif action == "dodge":
            print("gun\n")
            return "death"

        elif action == "tell a joke":
            print "not bad"
            return "laser_weapon_armory"
        elif action == 'fight':
            print 'dare you'
            return 'fight'

        else:
            print "do not compute"
            return "central_corridor"


class LaserWeaponArmory(Scene):

    def __enter__(self):
        print "input the password"
        code = "%d%d%d" % (randint(1, 1), randint(1, 1), randint(1, 1))
        for i in range(10):
            print "bzzzzd"
            guess = raw_input("[keypad]>>>")
            if code == guess:
                print "yes"
                return 'the_bridge'
            elif i < 9:
                print "try again"
            else:
                print "sb,you can die"
                return 'death'


class Fighting(Scene):

    def __enter__(self):
        print "i'll kick you ass off"
        solder_health = 100
        gothon_health = 100
        while solder_health > 0 or gothon_health > 0 :
            print "看招，sb士兵"
            solder_health = solder_health - randint(1, 9)
            print "看招，sb高特人"
            gothon_health = gothon_health - randint(1, 9)
        if solder_health > gothon_health:
            print "brave solder"
            return 'laser_weapon_armory'
        elif solder_health == gothon_health:
            print "再来"
            return 'fight'
        else:
            print "solder, you suck, prepare to die"
            return 'death'


class TheBridge(Scene):

    def __enter__(self):
        print "say bridge"

        action = raw_input(">")

        if action == "throw the bomb":
            print "it gose off"
            return 'death'
        elif action == 'slowly place the bomb':
            print "get off this thin can"
            return "escape_pod"
        else:
            print "does not compute"
            return "the_bridge"


class EscapePod(Scene):

    def __enter__(self):
        print "do you take?"
        good_pod = randint(1, 1)
        guess = raw_input("[pod#]>")
        if int(guess) != good_pod:
            print "into jam jelly"
            return 'death'
        else:
            print "time. you won"
            return 'finished'


class Finish(Scene):

    def __enter__(self):
        print "bravo"
        exit(1)


class Map(object):

    scene = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'fight': Fighting(),
        'finished': Finish()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scene.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
