def number():
    l=[5,9,7,2,6]
    x, y =5, 6
    i, j = l.index(x), l.index(y)
    l[i], l[j] = l[j], l[i]
    return (l)
print(number())