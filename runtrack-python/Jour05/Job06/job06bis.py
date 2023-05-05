print("""Jour 05 - JOb 06
      \nLuke Skywalker, un professeur de Math, fait passer un test et décide de noter
      \rses élèves sur une échelle allant de 0 à 100 inclus.
      \nSi un étudiant obtient moins de 40 sur 100, il échoue au test.
      \nS'il a plus de 40, il réussit le test.
      \nLuke est un professeur fort sympathique et décide donc d'arrondir à la hausse
      \nles notes des étudiants ayant réussi le test.
      \rMais Luke n'est quand même pas trop gentil. Cet arrondi à la hausse ne bénéficiera
      \rqu'aux étudiants remplissant certains critères, car tout de même, il ne faut pas
      \rexagérer, sans blague.
      \nLe critère est simple : Si un étudiant a eu une note de moins de strictement 3 points
      \rde son prochain multiple de 5, alors sa note est arrondie à ce multiple de 5.
      \nPar exemple,\n\n\tun 83 sera arrondi à 85 alors qu'un 82 restera un 82.
      \nPour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre une
      \rliste de notes et qui renvoie une liste de notes, arrondies comme il se doit,
      \rquand cela est nécessaire.\n"""
      )

list_note=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,41,52,63,74,82,83,84,85,86,96]
list_note_arrond=[]


for i in list_note:    
    if i%5==0:
        j=i+5
        if (j-i) < 3:
            list_note_arrond.append(j)
        else:
            list_note_arrond.append(i)
    elif i%5==1:
        j=i+4
        if (j-i) < 3:
            list_note_arrond.append(j)
        else:
            list_note_arrond.append(i)
    elif i%5==2:
        j=i+3
        if (j-i) < 3:
            list_note_arrond.append(j)
        else:
            list_note_arrond.append(i)
    elif i%5==3:
        j=i+2
        if (j-i) < 3:
            list_note_arrond.append(j)
        else:
            list_note_arrond.append(i)
    elif i%5==4:
        j=i+1
        if (j-i) < 3:
            list_note_arrond.append(j)
        else:
            list_note_arrond.append(i)
        

print(list_note)   
print(list_note_arrond)


