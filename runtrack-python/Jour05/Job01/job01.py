print("""Jour 05 - JOb 01
      \nCréez un programme qui demande à l'utilisateur de renseigner son prénom
      \nvia l'invite de commande grâce à la fonction input(). Le programme doit
      \nalors afficher dans le terminal “Hello xx !” ou xx est le prénom entré par l'utilisateur."""
      )

def ask_firstname():
    text = input("Quel est votre prénom ? : ")
    print("Hello " + text)

ask_firstname()
