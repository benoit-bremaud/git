print("""Jour 05 - JOb 03
      \nÉcrire une fonction qui, recevant une taille n en paramètre,
      \naffiche un tapis de n+1 lignes/n+1 colonnes traversé par une diagonale."""
      )

def draw_tapis(X):
    print("+" + "-" * (X) + "+")
    for i in range(X):
        print("|" + "#" * (X-1-i) + " " + "#" * i + "|")
    print("+" + "-" * (X) + "+")
    
draw_tapis(int(input("taille : ")))
