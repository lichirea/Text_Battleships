import unittest

from repo.maprepo import MapRepo


class MapService:
    def __init__(self):
        self._map = MapRepo()

    def place(self, x, y, length, orientation):
        """
        Places the corresponding ship on the board
        :param x:
        :param y:
        :param length:
        :param orientation:
        :return:
        """
        placeholder = self._map.copymap()
        try:
            y = int(y) - 1
        except ValueError:
            raise ValueError("Invalid coordinates")
        if x < 'A' or x > 'J' or len(x) != 1:
            raise ValueError("Invalid coordinates")
        else:
            x = ord(x) - 65
        if not isinstance(orientation, str):
            raise ValueError("Invalid orientation")
        elif orientation not in ['v', 'h']:
            raise ValueError("Invalid orientation")
        try:
            self._map.place(x, y, length, orientation)
        except ValueError as ve:
            self._map.setmap(placeholder)
            raise ValueError(ve)
        return "nice"

    def hit(self, x, y):
        # Checks what the shot did
        try:
            y = int(y) - 1
        except ValueError:
            raise ValueError("Invalid coordinates")
        if x < 'A' or x > 'J' or len(x) != 1:
            raise ValueError("Invalid coordinates")
        else:
            x = ord(x) - 65
        try:
            result = self._map.fire(x, y)
        except ValueError as ve:
            raise ve
        return result

    def getmap(self):
        # Returns the map
        return self._map.getmap()

    def getships(self):
        # Returns the number of ship parts to be hit remaining
        return self._map.getships()

    def hide(self, a):
        # Hides the enemy ships so the map can be shown to the player
        for i in range(10):
            for j in range(10):
                if a[i][j] == 'S':
                    a[i][j] = ' '
        return a

class testMapRepo(unittest.TestCase):

    def testhide(self):
       a = MapService()
       map = a._map.getmap()
       map[1][1] = 'S'
       a = a.hide(map)
       assert map[1][1] == ' '

    def testplace(self):
        a = MapService()
        self.assertRaises(ValueError, a.place, 'G', 8, 5, 'h')