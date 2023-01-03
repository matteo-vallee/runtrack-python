import math
def triangle(a,b,c):
    if (a+b > c) and (a+c > b) and (b+c > a):
        if (a == b == c):
            return ("c'est un triangle équilatéral")
        elif (a == b) or (a == c) or (b == c):
            if (a**2 + b**2 == int(c**2)) or (a**2 + c**2 == int(b**2)) or (b**2 + c**2 == int(a**2)):
                return ("c'est un triangle rectangle et isocèle")
            else:
                return ("c'est un triangle isocèle")
        elif (a**2 + b**2 == int(c**2)) or (a**2 + c**2 == int(b**2)) or (b**2 + c**2 == int(a**2)):
            return ("c'est un triangle rectangle")
        else:
            return ("c'est un triangle quelconque")
    else:
        return ("le triangle n'est pas constructible")

print(triangle(2,2,2))
print(triangle(3,4,7))
print(triangle(1,1,math.sqrt(2)))
print(triangle(3,4,5))
print(triangle(3,3,5))