import unittest
import random

import texttable

from repo.maprepo import MapRepo


class AIService:
    def __init__(self, x):
        self._map = x
        self._tactic = "random"
        self._tactics = ["right", "left", "up", "down", "random"]
        self._index = 0
        self._previous = [0, 0]

    def setup(self, me):
        """
        Randomly places the ships on the board
        :param me:
        :return:
        """
        done = False
        while not done:
            try:
                x = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
                y = random.randint(1, 9)
                o = random.choice(['h', 'v'])
                me.place(x, y, 5, o)
                done = True
            except ValueError:
                pass
        done = False
        while not done:
            try:
                x = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
                y = random.randint(1, 9)
                o = random.choice(['h', 'v'])
                me.place(x, y, 4, o)
                done = True
            except ValueError:
                pass
        done = False
        while not done:
            try:
                x = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
                y = random.randint(1, 9)
                o = random.choice(['h', 'v'])
                me.place(x, y, 4, o)
                done = True
            except ValueError:
                pass
        done = False
        while not done:
            try:
                x = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
                y = random.randint(1, 9)
                o = random.choice(['h', 'v'])
                me.place(x, y, 3, o)
                done = True
            except ValueError:
                pass

    def turn(self, player):
        """
        Fires at a random position :(((
        :param player:
        :return:
        """
        res = None
        if self._tactic == "random":
            done = False
            while not done:
                try:
                    x = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
                    y = random.randint(1, 9)
                    res = player.hit(x, y)
                    done = True
                except ValueError:
                    pass
        return res
