def count():
    j=0
    L=[8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    while j < len(L):
        L[j]=L[j]+1
        j+=1
    return(L)
print(count())