# JOB09 bis
txt="la plateforme, c'est super !"
if "e" in txt:
    x = txt.count("e")
    myorder = "La lettre 'e' est présente {} fois dans le texte."
    print(myorder.format(x))
if "o" not in txt:
    print("La lettre 'u' n'est pas présente dans le texte")