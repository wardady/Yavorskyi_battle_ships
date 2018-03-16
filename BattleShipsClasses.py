import string
from random import randint
import BattleShipsMethods


class Player:
    def __init__(self, name):
        self.__name = name

    def read_position(self):
        cords = ('', 0)
        while cords[0] not in string.ascii_uppercase and 0 < cords[1] < 11:
            cords = input("{}, enter move:".format(self.__name))
        a = (cords[0], int(cords[1] - 1))
        return a


class Ship:
    def __init__(self, bow, horizontal, length, hit=[]):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        if hit != []:
            self.__hit = hit
        else:
            self.__hit = [False for i in range(length)]

    def shoot_at(self, tup):
        if self.horizontal and (abs(65 - ord(tup[0]) - (
                    65 - ord(self.bow[0]))) < self.__length):
            self.__hit[ord(tup[0]) - ord(self.bow[0])] = True
            return True
        elif not self.horizontal and (
                            tup[1] - 1 - self.bow[1] < self.__length):
            self.__hit[tup[1] - 1 - self.bow[1]] = True
            return True
        return False


class Field:
    def __init__(self):
        self.field, ships = BattleShipsMethods.generate_field()
        self.__ships = [Ship((chr(65 + i[1]), i[0]), i[2], i[3]) for i in
                        ships]
        self.shooted = []

    def shoot_at(self, tup):
        self.shooted.append(tup)
        for ship in self.__ships:
            if ship.shoot_at(tup):
                self.field[ship.bow[1]][65 - ord(ship.bow[0])] = "X"
                return 1
        self.field[ship.bow[1]][65 - ord(ship.bow[0])] = "·"
        return 0

    def field_without_ships(self):
        fld = self.field[:]
        for i in range(10):
            for j in range(10):
                if (chr(65 + j), i + 1) not in self.shooted:
                    fld[chr(65 + j)][i] = " "
        st = " ".join(string.ascii_uppercase) + '\n'
        for n in range(1, 11):
            st += str(n) + ''.join(fld[n - 1]) + '\n'
        return st

    def field_with_ships(self):
        fld = self.field[:]
        for cell in self.shooted:
            if fld[cell[1] - 1][65 - ord(cell[0])] != 'X':
                fld[cell[1] - 1][65 - ord(cell[0])] = '·'
        st = " ".join(string.ascii_uppercase) + '\n'
        for n in range(1, 11):
            st += str(n) + ''.join(fld[n - 1]) + '\n'
        return st


class Game:
    def __init__(self):
        self.__field = [Field(), Field()]
        self.__players = [Player(input("Enter your name:")) for i in range(2)]
        self.__current_player = randint(0, 1)

    def read_position(self):
        return self.__players[self.__current_player].read_position()

    def shoot_at(self, ind, pos):
        self.__field[ind].shoot_at(pos)

    def field_without_ships(self, ind):
        return self.__field[ind].field_without_ships()

    def field_with_ships(self, ind):
        return self.__field[ind].field_with_ships()
