def count():
    i=0
    j=0
    L=[8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    while j <= 9:
        if L[j]%2 ==0:
          i= i + L[j]
        j+=1
    print(i)
count()
