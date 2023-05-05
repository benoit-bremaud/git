print("""Jour 05 - JOb 02
      \nÉcrire un programme qui affiche dans le terminal un rectangle
      \navec des '-' et des '|' en fonction des paramètres d'entrées,
      \n(width, height), par exemple : draw_rectangle(10, 3)
      \n\t|--------|
      \t|        |
      \t|--------|"""
      )

def draw_rextangle(X,Y):
    print("|" + "-" * (X-2) + "|")
    for i in range(Y-2):
        print("|" + " " * (X-2) + "|")
    print("|" + "-" * (X-2) + "|")
    
draw_rextangle(int(input("width : ")),int(input("height : ")))
