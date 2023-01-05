def count():
    j=0
    L= [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    max_val=L[0]
    min_val=L[0]
    while j < len(L):
        if L[j]> max_val:
            max_val=L[j]
        if L[j]< min_val:
            min_val=L[j]
        j+=1
    print(max_val)
    print(min_val)
count()
