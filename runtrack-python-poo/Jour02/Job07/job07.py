from gamer import *
from deck import *


def get_card(sabot):
    sabot.pop()
    return sabot[-1]


def pts_card(card, score):
    pts = 0
    if card[0].isalpha():
        if card[0] == "A":
            if int(score) > 11:
                pts += 1
            else:
                pts += 11
        else:
            pts += 10
    else:
        if int(card[0]) > 1:
            pts += int(card[0])
        else:
            pts += 10
    return pts

def get_play_again(texte):
    userInput = input(f"{texte} O/N : ").upper()
    
    if userInput == "N":
        return False
    elif userInput == "O":
        return True
    else:
        return get_play_again(texte)


play_again = True

while play_again:
    # nb_joueur = input("Combien de joueur ? (7 max) : ")
    print("\n---------NOUVEAU JEU---------\n")

    deck = Deck()
    sabot = deck.get_deck()
    
    
    player1 = Gamer("Benoit", [], 0)
    # player1.set_name("Benoit")
    bank = Gamer("Bank", [], 0)
    # bank.set_name("Bank")

    # print(len(sabot))
    card = get_card(sabot) # prendre une carte du sabot
    player1.set_hand(card) # la donner au joueur
    score = player1.get_pts() # noter les points de cette carte
    player1.set_pts(pts_card(card, score)) # ajoute les points à la main du joueur

    card = get_card(sabot) # prendre une carte dans le sabot
    bank.set_hand(card) # la donner à la banque
    score = bank.get_pts() # noter els points de cette carte
    bank.set_pts(pts_card(card, score)) # ajoute les points à la main de la banque
    print(bank.get_name()) # affiche le nom du joueur 'bank' -> bank
    print(bank.get_hand()) # affiche la carte
    print(bank.get_pts(), "points\n") # affiche les points en cours

    card = get_card(sabot)
    player1.set_hand(card)
    score = player1.get_pts()
    player1.set_pts(pts_card(card, score))
    print(player1.get_name())
    print(player1.get_hand())
    score = player1.get_pts()
    print(score, "points\n")
    if score == 21:
        print("Black Jack !!!")

    choice = True
    while choice:
        if get_play_again("Voulez-vous une carte ?"):
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
   
    play_again = get_play_again("Voulez-vous rejouer ?")
