import random
import sys

AI_TURN = True
USER_TURN = False

win_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 4, 8), (2, 4, 6), (0, 3, 6),
             (1, 4, 7), (2, 5, 8)]
bot = [0, 1, 2, 3, 4, 5, 6, 7, 8]
field = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']
dic = {"1 1": 0, "1  1": 0, "1  2": 1, "1 2": 1, "1 3": 2, "1  3": 2, "2 1": 3, "2  1": 3, "2 2": 4, "2  2": 4,
       "2 3": 5,
       "2  3": 5, "3 1": 6, "3  1": 6, "3 2": 7, "3  2": 7, "3 3": 8, "3  3": 8}

EMPTY_CHAR = "_"


def print_field():
    print('---------')
    print('|', field[0], field[1], field[2], '|')
    print('|', field[3], field[4], field[5], '|')
    print('|', field[6], field[7], field[8], '|')
    print('---------')


def check(coordinates):
    try:
        if field[dic[coordinates]] != '_':
            print("This cell is occupied! Choose another one!")
            return False
        else:
            return True
    except KeyError:
        try:
            first, second = coordinates.split(' ')
            if first and second not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                print("You should enter numbers!")
                return False
            elif first not in ('1', '2', '3') or second not in ('1', '2', '3'):
                print("Coordinates should be from 1 to 3!")
                return False
            else:
                return True
        except ValueError:
            print("You should enter numbers!")
            return False



