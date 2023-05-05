from gamer import *
from deck import *


def get_card(x):
    x.pop()
    return x[-1]


def pts_card(cards, var2):
    pts = 0
    if cards[0].isalpha():
        if cards[0] == "A":
            if int(var2) + 11 > 21:
                pts += 1
            else:
                pts += 11
        else:
            pts += 10
    else:
        if cards[0] == 1:
            pts += 10
        else:
            pts += int(card[0])
    return pts


play_again = True

while play_again:
    nb_joueur = input("Combien de joueur ? (7 max) : ")

    deck = Deck()
    sabot = deck.get_deck()
    player1 = Gamer("Benoit", [], 0)
    # player1.set_name("Benoit")
    bank = Gamer("Bank", [], 0)
    # bank.set_name("Bank")

    # print(len(sabot))
    player1.set_hand(get_card(sabot))
    score = player1.get_pts()
    player1.set_pts(pts_card(card, score))

    # print(len(sabot))

    bank.set_hand(get_card(sabot))
    score = bank.get_pts()
    bank.set_pts(pts_card(card, score))
    print(bank.get_name())
    print(bank.get_hand(), "\n")
    # bank.get_all_info()

    # print(len(sabot))
    player1.set_hand(get_card(sabot))
    score = player1.get_pts()
    player1.set_pts(pts_card(card, score))
    print(player1.get_name())
    print(player1.get_hand())
    print(player1.get_pts(), "\n")
    # player1.get_all_info()

    choice = True
    while choice:
        if input("\nSouhaitez-vous une carte supplémentaire ? O/N : ") == "O":
            # print(len(sabot))
            card = get_card(sabot)
            player1.set_hand(card)
            score = player1.get_pts()
            player1.set_pts(pts_card(card, score))
            print(player1.get_name())
            print(player1.get_hand())
            print(player1.get_pts(), "\n")
            # player1.get_all_info()
            if player1.get_pts() > 21:
                break
        else:
            choice = False

    if player1.get_pts() <= 21:
        while bank.get_pts() < 17 and bank.get_pts() < 21:
            card = get_card(sabot)
            bank.set_hand(card)
            score = bank.get_pts()
            bank.set_pts(pts_card(card, score))
            print(bank.get_name())
            print(bank.get_hand())
            print(bank.get_pts(), "\n")
            # bank.get_all_info()
    else:
        pass

    if player1.get_pts() > 21:
        print("Vous avez perdu votre mise !")
    elif bank.get_pts() > 21:
        print("La banque saute, vous avez gagné !")
    elif bank.get_pts() > player1.get_pts():
        print("Vous avez perdu votre mise !")
    elif bank.get_pts() == player1.get_pts():
        print("Egalité, vous ne perdez pas votre mise !")
    else:
        pass

    if input("Rejouer ? O/N : ") == "N":
        play_again = False
    else:
        pass
