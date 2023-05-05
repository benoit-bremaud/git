print("""Jour 05 - JOb 05
      \nUn gardien de phare va aux toilettes cinq fois par jour.
      \rOr les WC sont au rez-de-chaussée...
      \nÉcrire une fonction qui reçoit en paramètres, le nombre de marches du phare
      \ret la hauteur de chaque marche (en cm), cette fonction doit calculer combien
      \rde mètre le gardien effectué par semaine pour aller aux toilettes.
      \nLa sortie du code doit être : Pour x marches de y cm, le gardien parcours z.zz m par semaine.
      \nOn n'oubliera pas :
      \n\tqu'une semaine comporte 7 jours ;
      \r\tqu'une fois en bas, le gardien doit remonter ;
      \r\tque le résultat est à exprimer en m.\n"""
      )

nb_marches=float(input("Nombre de marche ?: "))
h_marche=float(input("La hauteur des marches (en cm) ?: "))

calcul=float((nb_marches * h_marche * 2 * 5 * 7))

print("Pour " + str(nb_marches) + " marches de " + str(h_marche) + " cm, le gardien parcours " + str(calcul*0.001) + " m par semaine")

