def calcule(num1,operator,num2):
    if (operator == "-"):
        res = num1 - num2
    elif (operator == "+"):
        res = num1 + num2
    elif (operator == "*"):
        res = num1 * num2
    elif (operator == "%"):
        res = num1 % num2
    elif (operator == "/"):
        res = num1 / num2
    return (res)

print(calcule(15,"+",38))
print(calcule(15,"*",38))
print(calcule(38,"%",15))
print(calcule(38,"-",15))
print(calcule(38,"/",15))