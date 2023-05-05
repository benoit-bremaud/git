import math
def triangletype(a,b,c):
    # permet de déterminer si le triangle est équilatéral
    if a == b == c:
        return "Equilatéral"

    # permet de définir si le triangle est isocèle et rectangle
    elif (a*a == b*b + c*c and b==c) or (b*b == c*c + a*a and c==a) or (c*c == a*a + b*b and b==a):
        return "Rectangle et isocèle"
    
    elif (a*a == b*b + c*c and b!=c) or (b*b == c*c + a*a and c!=a) or (c*c == a*a + b*b and b!=a):
        return "Rectangle"

    elif a==b or b==c or c==a:
        return "Isocèle"
    else:
        return "C'est un triangle quelconque"

print(triangletype(5,5,5))
print(triangletype(4,5,3))
print(triangletype(6,6,6))
print(triangletype(5,3,4))
print(triangletype(8,8,12))
print(triangletype(9,9,math.sqrt(162)))
print(triangletype(9,9,math.sqrt(162)))
print(triangletype(9,9,math.sqrt(162)))
print(triangletype(6,math.sqrt(72.0),6))