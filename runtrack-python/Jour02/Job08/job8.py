def typesaison(type,saison):
    if type == "fruits" and saison == "hiver":
        return "Orange, Mandarine et Kiwi"
    if type == "fruits" and saison == "ete":
        return "Poire, Fraise, cassis"
    if type == "legume" and saison == "hiver":
        return "Carotte, Topinambour, Endive"
    if type == "legume" and saison == "ete":
        return "Artichaut, Aubergine, Navet"
print(typesaison("fruits","hiver"))
print(typesaison("fruits","ete"))
print(typesaison("legume","hiver"))
print(typesaison("legume","ete"))
