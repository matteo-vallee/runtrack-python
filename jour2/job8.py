def Bio_Marcket(type,saison):
    if (type == "fruits") and (saison == "hiver"):
        return ("Orange,Mandarine,Kiwi")
    elif (type == "fruits") and (saison == "ete"):
        return ("Poire,Fraise,Cassis")
    elif (type == "legume") and (saison == "hiver"):
        return ("carotte,topinambour,endive")
    elif (type == "legume") and (saison == "ete"):
        return ("artichaut,aubergine,navet")



print(Bio_Marcket("fruits","hiver"))
print(Bio_Marcket("fruits","ete"))
print(Bio_Marcket("legume","hiver"))
print(Bio_Marcket("legume","ete"))