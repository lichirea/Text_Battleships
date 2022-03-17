import unittest

from domain.map import Map


class MapRepo:
    def __init__(self):
        self._map = Map()
        self._ships = 16

    def fire(self, x, y):
        """
        Analyses the given coordinates and sets them as hit
        :param x:
        :param y:
        :return: the result
        """
        if x > 9 or y > 9 or x < 0 or y < 0:
            raise ValueError("Can't fire a shot out of bounds!")
        if self._map.map[x][y] == ' ':
            self._map.map[x][y] = 'O'
            return "miss"
        elif self._map.map[x][y] == 'S':
            self._map.map[x][y] = 'X'
            self._ships -= 1
            return "ship"
        elif self._map.map[x][y] == 'O':
            return "already missed"
        elif self._map.map[x][y] == 'X':
            return "already hit"

    def place(self, x, y, length, orientation):
        """
        Places a ship with the top left corner in (x,y)
        :param x:
        :param y:
        :param length: of the ship
        :param orientation: of the ship
        :return:
        """
        if x+length > 10 and orientation == 'h' or y + length > 10 and orientation == 'v':
            raise ValueError("Can't place a ship out of bounds!")
        if orientation == 'h':
            for i in range(length):
                if self._map.map[x+i][y] == 'S':
                    raise ValueError("There's already another ship in the way!")
                else:
                    self._map.map[x+i][y] = 'S'
        if orientation == 'v':
            for i in range(length):
                if self._map.map[x][y+i] == 'S':
                    raise ValueError("There's already another ship in the way!")
                else:
                    self._map.map[x][y+i] = 'S'

    def getmap(self):
        return self._map.map

    def copymap(self):
        return self._map.map.copy()

    def setmap(self, value):
        self._map.map = value

    def getships(self):
        return self._ships


class testMapRepo(unittest.TestCase):

    def testhit(self):
       a = MapRepo()
       self.assertRaises(ValueError, a.fire, 5, 11)
       self.assertRaises(ValueError, a.fire, 11, 5)
       a.fire(1, 1)
       assert a.fire(1, 1) == "already missed"

    def testplace(self):
        a = MapRepo()
        a.place(0, 0, 3, 'h')
        for i in range(3):
            assert a._map.map[i][0] == 'S'
