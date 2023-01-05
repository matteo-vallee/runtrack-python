def count():
    i=0
    j=0
    L=[8,24,48,2,16]
    while j < 4:
        if L[j]%3 ==0:
            i+=1
        j+=1
    print(i)
count()
