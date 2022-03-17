import texttable

from service.AIService import AIService
from service.mapservice import MapService


class Console:
    def __init__(self):
        self._player = MapService()
        self._enemy = MapService()
        self._ai = AIService(self._enemy)
        print("Game initialized")
        self.printboard()
        self.setup()

    def printboard(self):
        print("\n\n\n ############################################\n\n\n")
        table = texttable.Texttable()
        placeholder = self._enemy.getmap()
        enemy = placeholder.copy()
        enemy = self._enemy.hide(enemy)
        table.header(['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        for i in range(10):
            table.add_row([i + 1, enemy[0][i], enemy[1][i], enemy[2][i],
                          enemy[3][i], enemy[4][i], enemy[5][i],
                          enemy[6][i], enemy[7][i], enemy[8][i],
                          enemy[9][i]])
        print(table.draw())

        print("=======================================================")

        table = texttable.Texttable()
        player = self._player.getmap()
        table.header(['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        for i in range(10):
            table.add_row([i + 1, player[0][i], player[1][i], player[2][i],
                          player[3][i], player[4][i], player[5][i],
                          player[6][i], player[7][i], player[8][i],
                          player[9][i]])
        print(table.draw())

    def setup(self):
        # Places all the ships on the player's board
        done = False
        while not done:
            try:
                print("Place your destroyer (length 5)")
                o = input("Input orientation (v/h): ")
                x = input("Input x coordinate: ")
                y = input("Input y coordinate: ")
                self._player.place(x, y, 5, o)
                done = True
                self.printboard()
            except ValueError as ve:
                print(ve)

        done = False
        while not done:
            try:
                print("Place your first cruiser (length 4)")
                o = input("Input orientation (v/h): ")
                x = input("Input x coordinate: ")
                y = input("Input y coordinate: ")
                self._player.place(x, y, 4, o)
                done = True
                self.printboard()
            except ValueError as ve:
                print(ve)

        done = False
        while not done:
            try:
                print("Place your second cruiser (length 4)")
                o = input("Input orientation (v/h): ")
                x = input("Input x coordinate: ")
                y = input("Input y coordinate: ")
                self._player.place(x, y, 4, o)
                done = True
                self.printboard()
            except ValueError as ve:
                print(ve)

        done = False
        while not done:
            try:
                print("Place your boat (length 3)")
                o = input("Input orientation (v/h): ")
                x = input("Input x coordinate: ")
                y = input("Input y coordinate: ")
                self._player.place(x, y, 3, o)
                done = True
                self.printboard()
            except ValueError as ve:
                print(ve)
        self.printboard()

        self._ai.setup(self._enemy)

        self.begin()

    def begin(self):
        # This represents the player's turn
        print("Ready to fire your shot!")
        done = False
        while not done:
            try:
                x = input("Input x coordinate of shot:")
                y = input("Input y coordinate of shot:")
                res = self._enemy.hit(x, y)
                print(res)
                print(self._enemy.getships())
                if self._enemy.getships() == 0:
                    self.win("player")
                done = True
            except ValueError as ve:
                print(ve)
        self.enemy_turn()

    def enemy_turn(self):
        # This represents the enemy's turn
        print(self._ai.turn(self._player))
        if self._player.getships() == 0:
            self.win("computer")
        self.printboard()
        self.begin()

    def win(self, who):
        # Is called when one of the players has no more ships to hit and the game is over
        print("\n\n========================\n The " + who + " has won!")
        raise SystemExit(0)
