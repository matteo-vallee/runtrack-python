def count():
    i=1
    j=0
    L=[8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    while j < len(L):
        if L[j] >= 25 and L[j] <=90:
            i=i*L[j]
        j+=1
    print(i)



count()