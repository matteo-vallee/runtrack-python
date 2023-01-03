def number_value(nombre):
    if (nombre < 0):
        return ("Negatif")
    elif (nombre > 0):
        return ("Positif")

print(number_value(15))
print(number_value(-15))
print(number_value(0.5))