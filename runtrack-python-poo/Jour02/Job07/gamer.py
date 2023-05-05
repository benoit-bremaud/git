class Gamer:
    def __init__(self, name="Player_1", hand=[], pts=0):
        self.name = name
        self.hand = hand
        self.points = pts

    def get_all_info(self):
        print(f"{self.name} avec les cartes : {self.hand}, totalise {self.points} points !")

    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand

    def get_pts(self):
        return self.points

    def set_name(self, name):
        self.name = name

    def set_hand(self, new_carte):
        self.hand += [new_carte]

    def set_pts(self, value):
        self.points += value
