def fonction(langage):
    if langage.lower() == "javascript":
        return "tu es un développeur web"
    if langage.lower() == "python":
        return "tu es un développeur IA"
    if langage.lower() == "java":
        return "tu es un développeur logiciel"
    if langage.lower() == "reactjs":
        return "Tu es un développeur mobile"
    else:
        return "Un jour je serai le meilleur développeur"
print(fonction("javascript"))
print(fonction("Javascript"))
print(fonction("python"))
print(fonction("PyThOn"))
print(fonction("java"))
print(fonction("reactjs"))
print(fonction("assembler"))
