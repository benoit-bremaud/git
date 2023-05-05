def calcule(num1,operator,num2):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    else:
        return "Seuls les opérateurs suivants sont valides : '+', '-', '*', '/' alors arrête d'écrire des conneries"
    
print(calcule(1,"+",2))
print(calcule(10,"-",5))
print(calcule(10,"*",10))
print(calcule(100,"/",5))
print(calcule(50,"++",5))


operator=input("Renseignez l'opérateur ")
num1=int(input("Renseignez numéro 1 "))
num2=int(input("Renseignez numéro 2 "))
if operator == "+":
    print(num1 + num2)
if operator == "-":
    print(num1 - num2)
if operator == "*":
    print(num1 * num2)
if operator == "/":
    print(num1 / num2)
else:
    print("Seuls les opérateurs suivants sont valides : '+', '-', '*', '/' alors arrête d'écrire des conneries")


password=input("Renseignez le mot de passe : ")
print(password)
