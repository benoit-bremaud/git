# JOB09 tri
txt="la plateforme, c'est super !"
lettercheck=input("Saisir lettre à chercher : ")
x = txt.count(lettercheck)
myorder = "La lettre {} est présente {} fois dans le texte."
print(myorder.format(lettercheck, x))