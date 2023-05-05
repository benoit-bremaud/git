import random
from random import shuffle


class Deck:
    val = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "A"]
    col = ["Pique", "Coeur", "Trefle", "Carreau"]

    def __init__(self, deck=[]):
        self.__deck = deck

    def get_deck(self):
        for val in Deck.val[::]:
            for col in Deck.col[::]:
                self.__deck += [val + col]
        random.shuffle(self.__deck)
        return self.__deck

